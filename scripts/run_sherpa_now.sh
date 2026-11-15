#!/usr/bin/env bash
set -euo pipefail

SHERPA_DIR="/Users/mineshwadhwa/Documents/Sherpa"
SCHEDULE_MGR="$SHERPA_DIR/scripts/schedule_manager.py"
AGENTAPI_BIN="/Users/mineshwadhwa/.gemini/antigravity/bin/agentapi"
TODAY_IST="$(TZ=Asia/Kolkata date +%Y-%m-%d)"

DRY_RUN=0
if [[ "${1:-}" == "--dry-run" ]]; then
  DRY_RUN=1
fi

ON_DEMAND_PROMPT="Run the full Sherpa LinkedIn Job Application Support System on demand in /Users/mineshwadhwa/Documents/Sherpa following /Users/mineshwadhwa/Documents/Sherpa/.agents/skills/run-sherpa/SKILL.md, /Users/mineshwadhwa/Documents/Sherpa/.agents/skills/job-application-workflow/SKILL.md, and /Users/mineshwadhwa/Documents/Sherpa/AGENTS.md. Execute Steps 1–6 (Gmail discovery with newer_than:7d and application detection with newer_than:14d, full LinkedIn JD retrieval via browser subagent, Canonical Master Profile v1.1.0 mapping & role fit assessment, tailored CV + PDF rendering + independent Fact-Check + ATS/Editorial audit + record validation, tracker update + dashboard rebuild via build_dashboard.py), ensure the cron schedule is moved 3 days ahead via schedule_manager.py, and present the summary for User Approval (Gate 9 — never submit applications automatically)."

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "[dry-run] Current schedule state:"
  python3 "$SCHEDULE_MGR" status
  echo "[dry-run] Would shift schedule +3 days via: python3 $SCHEDULE_MGR advance --mode on_demand"
  echo "[dry-run] Would launch: $AGENTAPI_BIN new-conversation --title=\"Sherpa On-Demand Run $TODAY_IST\" -- \"$ON_DEMAND_PROMPT\""
  exit 0
fi

echo "Shifting Sherpa cron schedule 3 days ahead from $TODAY_IST..."
python3 "$SCHEDULE_MGR" advance --mode on_demand

echo "Launching on-demand Sherpa workflow conversation..."
exec "$AGENTAPI_BIN" new-conversation \
  --title="Sherpa On-Demand Run $TODAY_IST" \
  -- "$ON_DEMAND_PROMPT"
