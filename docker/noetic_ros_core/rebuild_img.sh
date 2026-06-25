#!/bin/bash
set -euo pipefail

# first_tag=ubuntu20250530
second_tag=ubuntu20260625

image="ozkrelo/noetic-ros-core:$second_tag"

docker build --no-cache -t "$image" .
# docker push "$image"
