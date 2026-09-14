#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly script_dir

# Keep this order aligned with the image hierarchy documented in README.md.
readonly -a build_directories=(
  focal_snapshot
  noetic_ros_core
  mir_robot
  mobipick
  mobipick_labs
  x_mobipick_labs
  host_user
)

# host_user is machine-specific and is intentionally not published.
readonly -a publishable_images=(
  ozkrelo/focal-snapshot:20260625
  ozkrelo/noetic-ros-core:ubuntu20260625
  ozkrelo/mir:noetic-v2.0
  ozkrelo/mobipick:noetic-v2.0
  ozkrelo/mobipick_labs:noetic-v2.0
  ozkrelo/x_mobipick_labs:noetic-v2.0
)

while true; do
  read -r -p "Push publishable images after all rebuilds succeed? [y/N] " reply || {
    printf '\nNo selection received; no rebuilds were started.\n' >&2
    exit 1
  }

  case "$reply" in
    [Yy]|[Yy][Ee][Ss])
      push_images=true
      break
      ;;
    ''|[Nn]|[Nn][Oo])
      push_images=false
      break
      ;;
    *)
      printf 'Please answer yes or no.\n' >&2
      ;;
  esac
done

for directory in "${build_directories[@]}"; do
  printf '\nRebuilding %s...\n' "$directory"
  if ! (cd "$script_dir/$directory" && time ./rebuild_img.sh); then
    printf '\nRebuild failed in %s; stopping. Nothing was pushed.\n' "$directory" >&2
    exit 1
  fi
done

if [[ "$push_images" == false ]]; then
  printf '\nAll images rebuilt successfully. Push was not requested.\n'
  exit 0
fi

printf '\nAll images rebuilt successfully. Pushing publishable images...\n'
for image in "${publishable_images[@]}"; do
  printf '\nPushing %s...\n' "$image"
  docker push "$image"
done

printf '\nAll publishable images were pushed successfully.\n'
