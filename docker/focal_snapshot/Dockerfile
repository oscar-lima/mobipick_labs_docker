FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
ARG SNAPSHOT=20250530T235959Z

# Use only the immutable Ubuntu Snapshot Service
RUN set -eux; \
  cat >/etc/apt/sources.list <<EOF
deb https://snapshot.ubuntu.com/ubuntu/${SNAPSHOT} focal main restricted universe multiverse
deb https://snapshot.ubuntu.com/ubuntu/${SNAPSHOT} focal-updates main restricted universe multiverse
deb https://snapshot.ubuntu.com/ubuntu/${SNAPSHOT} focal-backports main restricted universe multiverse
deb https://snapshot.ubuntu.com/ubuntu/${SNAPSHOT} focal-security main restricted universe multiverse
EOF

# 1) Bootstrap once: temporarily disable TLS verification to fetch CA + keyring
RUN set -eux; \
  rm -rf /var/lib/apt/lists/*; mkdir -p /var/lib/apt/lists/partial; \
  printf '%s\n' \
'Acquire::http::No-Cache "true";' \
'Acquire::https::No-Cache "true";' \
'Acquire::http::Pipeline-Depth "0";' \
'Acquire::Check-Valid-Until "false";' \
'Acquire::https::Verify-Peer "false";' \
'Acquire::https::Verify-Host "false";' \
  > /etc/apt/apt.conf.d/00-bootstrap; \
  apt-get update -o Acquire::CompressionTypes::Order::=gz; \
  apt-get install -y --no-install-recommends ca-certificates ubuntu-keyring; \
  rm -f /etc/apt/apt.conf.d/00-bootstrap

# 2) Normal operation with verification on, still pinned to the snapshot
RUN set -eux; \
  printf '%s\n' \
'Acquire::http::No-Cache "true";' \
'Acquire::https::No-Cache "true";' \
'Acquire::http::Pipeline-Depth "0";' \
'Acquire::Check-Valid-Until "false";' \
  > /etc/apt/apt.conf.d/99-freeze; \
  rm -rf /var/lib/apt/lists/*; \
  apt-get update -o Acquire::CompressionTypes::Order::=gz; \
  rm -rf /var/lib/apt/lists/*

# example installs (keep using the snapshot lists)
# RUN apt-get update && apt-get install -y --no-install-recommends <packages> && rm -rf /var/lib/apt/lists/*
