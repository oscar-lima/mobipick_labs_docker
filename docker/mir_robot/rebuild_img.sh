#!/bin/bash
set -euo pipefail

# first_tag=noetic
second_tag=noetic-v2.0

image="ozkrelo/mir:$second_tag"

docker build --no-cache -t "$image" .
# docker push "$image"
