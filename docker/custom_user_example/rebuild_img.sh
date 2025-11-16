#!/bin/bash

tag="$USER"_user_from_1.2

# Build the Docker image inheriting UID and GID from the host user
# to avoid permission issues with mounted volumes.
docker build \
  --build-arg USER="$USER" \
  --build-arg UID="$(id -u)" \
  --build-arg GID="$(id -g)" \
  -t ozkrelo/x_mobipick_labs:$tag .
