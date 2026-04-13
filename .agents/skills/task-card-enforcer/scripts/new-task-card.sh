#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../../../.." && pwd)"
cat "$ROOT/docs/templates/TASK_CARD_TEMPLATE.md"
