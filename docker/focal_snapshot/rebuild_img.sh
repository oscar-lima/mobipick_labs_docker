#!/bin/bash
set -euo pipefail

# tag is the build date in format: YYYYMMDD

# first_tag=20250530
second_tag=20260625

image="ozkrelo/focal-snapshot:$second_tag"

docker build --no-cache --pull -t "$image" .
# docker push "$image"
