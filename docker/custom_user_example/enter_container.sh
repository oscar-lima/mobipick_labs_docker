#!/usr/bin/env bash
set -euo pipefail

# Go to the directory containing this script and docker-compose.yml
cd "$(dirname "${BASH_SOURCE[0]}")"

# Run the custom_user service with an interactive bash shell.
# --rm removes the container when you exit.
docker compose run --rm custom_user bash
