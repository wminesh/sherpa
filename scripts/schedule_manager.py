#!/usr/bin/env python3
"""
Manages the dynamic 3-day cron schedule for the Sherpa Job Application Workflow.

Whenever the workflow runs (either on-demand or via scheduled automation),
`advance` shifts the next scheduled run to `run_date + 3 days` at 12:00 PM IST
in both `tracker/schedule_state.json` and the Antigravity sidecar config
(`~/.gemini/config/sidecars/linkedin-job-application-workflow/sidecar.json`).

`check-due` guards scheduled runs against firing early if Antigravity has not
yet reloaded an updated `sidecar.json`.
"""

import argparse
import calendar
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

DEFAULT_TZ = "Asia/Kolkata"
DEFAULT_INTERVAL_DAYS = 3
DEFAULT_HOUR = 12
DEFAULT_MINUTE = 0

BASE_DIR = Path("/Users/mineshwadhwa/Documents/Sherpa")
DEFAULT_STATE_PATH = BASE_DIR / "tracker" / "schedule_state.json"
DEFAULT_SIDECAR_PATH = Path(
    "/Users/mineshwadhwa/.gemini/config/sidecars/linkedin-job-application-workflow/sidecar.json"
)


def compute_cron_expression(
    run_date: date,
    target_date: date,
    hour: int = DEFAULT_HOUR,
    minute: int = DEFAULT_MINUTE,
    tz_name: str = DEFAULT_TZ,
    interval_days: int = DEFAULT_INTERVAL_DAYS,
) -> str:
    """Build a 5-field CRON_TZ expression starting on `target_date`."""
    _, days_in_month = calendar.monthrange(target_date.year, target_date.month)
    day_list = list(range(target_date.day, days_in_month + 1, interval_days))
    days_field = ",".join(str(d) for d in day_list)

    # Pin the month when crossing a month boundary so later days in `run_date`'s
    # month cannot trigger early (e.g., Feb 26 -> Mar 1 must not match Feb 28).
    month_field = "*" if target_date.month == run_date.month else str(target_date.month)
    return f"CRON_TZ={tz_name} {minute} {hour} {days_field} {month_field} *"


def read_json(path: Path) -> dict:
    """Return parsed JSON from `path`, or an empty dict if missing."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    """Atomically write formatted JSON to `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def update_sidecar_schedule(
    sidecar_path: Path,
    cron_expr: str,
    target_date: date,
    hour: int,
    minute: int,
    tz_name: str,
    interval_days: int,
) -> dict:
    """Update `args[0]` and `description` in `sidecar.json` if it exists."""
    if not sidecar_path.exists():
        return {"updated": False, "reason": f"Sidecar file not found: {sidecar_path}"}

    data = read_json(sidecar_path)
    args = data.get("args", [])
    previous_cron = args[0] if args else None
    if args:
        args[0] = cron_expr
        data["args"] = args

    time_label = f"{hour:02d}:{minute:02d}"
    data["description"] = (
        f"Next run: {target_date.isoformat()} at {time_label} ({tz_name}), repeating every "
        f"{interval_days} days. Scans Gmail for new LinkedIn PM job alerts and application "
        f"confirmations, evaluates fit against the Canonical Master Profile (v1.1.0), generates "
        f"fact-checked tailored PDF CVs, updates the tracker, and rebuilds the dashboard."
    )
    write_json(sidecar_path, data)
    return {
        "updated": True,
        "sidecar_path": str(sidecar_path),
        "previous_cron": previous_cron,
        "new_cron": cron_expr,
    }


def cmd_advance(args: argparse.Namespace) -> int:
    """Shift `next_scheduled_date` to `run_date + interval_days` and update cron."""
    tz = ZoneInfo(args.tz)
    now_local = datetime.now(tz)
    run_date = date.fromisoformat(args.date) if args.date else now_local.date()
    target_date = run_date + timedelta(days=args.days)

    cron_expr = compute_cron_expression(
        run_date=run_date,
        target_date=target_date,
        hour=args.hour,
        minute=args.minute,
        tz_name=args.tz,
        interval_days=args.days,
    )
    next_run_dt = datetime(
        target_date.year, target_date.month, target_date.day, args.hour, args.minute, tzinfo=tz
    )

    state = {
        "timezone": args.tz,
        "interval_days": args.days,
        "run_hour": args.hour,
        "run_minute": args.minute,
        "last_run_at": now_local.isoformat(timespec="seconds"),
        "last_run_date": run_date.isoformat(),
        "last_run_mode": args.mode,
        "next_scheduled_date": target_date.isoformat(),
        "next_scheduled_at": next_run_dt.isoformat(timespec="seconds"),
        "cron_expression": cron_expr,
    }
    state_path = Path(args.state_path)
    write_json(state_path, state)

    sidecar_result = update_sidecar_schedule(
        sidecar_path=Path(args.sidecar_path),
        cron_expr=cron_expr,
        target_date=target_date,
        hour=args.hour,
        minute=args.minute,
        tz_name=args.tz,
        interval_days=args.days,
    )

    print(
        json.dumps(
            {
                "action": "advance",
                "state_path": str(state_path),
                "state": state,
                "sidecar": sidecar_result,
            },
            indent=2,
        )
    )
    return 0


def cmd_check_due(args: argparse.Namespace) -> int:
    """Check whether today's date has reached `next_scheduled_date`."""
    tz = ZoneInfo(args.tz)
    now_local = datetime.now(tz)
    today = date.fromisoformat(args.date) if args.date else now_local.date()

    state_path = Path(args.state_path)
    state = read_json(state_path)
    next_str = state.get("next_scheduled_date")

    if not next_str:
        print(
            json.dumps(
                {
                    "due": True,
                    "today": today.isoformat(),
                    "next_scheduled_date": None,
                    "reason": "No prior schedule state found; proceeding.",
                },
                indent=2,
            )
        )
        return 0

    next_date = date.fromisoformat(next_str)
    is_due = today >= next_date
    reason = (
        f"Today ({today.isoformat()}) is on or after next_scheduled_date ({next_str}); proceeding."
        if is_due
        else (
            f"Today ({today.isoformat()}) is before next_scheduled_date ({next_str}) "
            f"(shifted {state.get('interval_days', DEFAULT_INTERVAL_DAYS)} days ahead from "
            f"{state.get('last_run_mode', 'prior')} run on {state.get('last_run_date', 'unknown')}). "
            f"Skip this trigger."
        )
    )
    print(
        json.dumps(
            {
                "due": is_due,
                "today": today.isoformat(),
                "next_scheduled_date": next_str,
                "last_run_date": state.get("last_run_date"),
                "last_run_mode": state.get("last_run_mode"),
                "reason": reason,
            },
            indent=2,
        )
    )
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    """Display current schedule state and sidecar cron configuration."""
    state = read_json(Path(args.state_path))
    sidecar = read_json(Path(args.sidecar_path))
    print(
        json.dumps(
            {
                "state_path": args.state_path,
                "state": state,
                "sidecar_path": args.sidecar_path,
                "sidecar_cron": sidecar.get("args", [None])[0],
            },
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sherpa 3-day rolling cron schedule manager")
    parser.add_argument("--tz", default=DEFAULT_TZ)
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH))
    parser.add_argument("--sidecar-path", default=str(DEFAULT_SIDECAR_PATH))

    sub = parser.add_subparsers(dest="command", required=True)

    p_adv = sub.add_parser("advance", help="Move next scheduled run +N days ahead from run date")
    p_adv.add_argument("--mode", choices=["on_demand", "scheduled"], required=True)
    p_adv.add_argument("--days", type=int, default=DEFAULT_INTERVAL_DAYS)
    p_adv.add_argument("--hour", type=int, default=DEFAULT_HOUR)
    p_adv.add_argument("--minute", type=int, default=DEFAULT_MINUTE)
    p_adv.add_argument("--date", default=None, help="Override run date (YYYY-MM-DD) for testing")
    p_adv.set_defaults(func=cmd_advance)

    p_chk = sub.add_parser("check-due", help="Check if scheduled run is due today")
    p_chk.add_argument("--date", default=None, help="Override today's date (YYYY-MM-DD) for testing")
    p_chk.set_defaults(func=cmd_check_due)

    p_stat = sub.add_parser("status", help="Show schedule state and sidecar cron")
    p_stat.set_defaults(func=cmd_status)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
