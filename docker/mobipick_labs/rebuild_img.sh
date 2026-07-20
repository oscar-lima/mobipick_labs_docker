#!/bin/bash
set -euo pipefail

version=2.0
tag=noetic-v$version

image="ozkrelo/mobipick_labs:$tag"

docker build --no-cache -t "$image" .
# docker push "$image"
