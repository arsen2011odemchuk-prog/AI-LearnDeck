#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 sandbox_core.py --host 0.0.0.0 --port 5050
