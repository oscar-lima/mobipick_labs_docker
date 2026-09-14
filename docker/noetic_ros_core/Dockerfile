# originally fetched from https://github.com/osrf/docker_images/blob/master/ros/noetic/ubuntu/focal/ros-core/Dockerfile
# This is an auto generated Dockerfile for ros:ros-core
# generated from docker_images/create_ros_core_image.Dockerfile.em
# FROM ubuntu:focal
ARG WAYLAND_VERSION=1.20.0
ARG WAYLAND_SHA256=b8a034154c7059772e0fdbd27dbfcda6c732df29cae56a82274f6ec5d7cd8725

FROM ozkrelo/focal-snapshot:20260625 AS wayland-builder

ARG WAYLAND_VERSION
ARG WAYLAND_SHA256

# NVIDIA EGL-Wayland v2 requires wl_proxy_marshal_flags, which is absent from
# Ubuntu Focal's Wayland 1.18 runtime.
RUN apt-get update && apt-get install -q -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        libexpat1-dev \
        libffi-dev \
        meson \
        ninja-build \
        pkg-config \
        xz-utils \
    && curl -fsSL \
        "https://wayland.freedesktop.org/releases/wayland-${WAYLAND_VERSION}.tar.xz" \
        -o /tmp/wayland.tar.xz \
    && echo "${WAYLAND_SHA256}  /tmp/wayland.tar.xz" | sha256sum -c - \
    && tar -C /tmp -xf /tmp/wayland.tar.xz \
    && meson setup /tmp/wayland-build "/tmp/wayland-${WAYLAND_VERSION}" \
        --prefix=/usr/local \
        --libdir=lib \
        -Ddocumentation=false \
        -Ddtd_validation=false \
        -Dscanner=true \
        -Dtests=false \
    && ninja -C /tmp/wayland-build \
    && DESTDIR=/wayland-root ninja -C /tmp/wayland-build install \
    && nm -D /wayland-root/usr/local/lib/libwayland-client.so.0 \
        | grep -q ' wl_proxy_marshal_flags$'

FROM ozkrelo/focal-snapshot:20260625

# setup timezone
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

# install packages
RUN apt-get update && apt-get install -q -y --no-install-recommends \
    ca-certificates \
    curl \
    dirmngr \
    gnupg2 \
    libdrm2 \
    libgbm1 \
    qtwayland5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=wayland-builder /wayland-root/usr/local/ /usr/local/
RUN set -eux; \
    dpkg --compare-versions \
        "$(dpkg-query -W -f='${Version}' libdrm2)" ge 2.4.99; \
    dpkg --compare-versions \
        "$(dpkg-query -W -f='${Version}' libgbm1)" ge 21.2; \
    ldconfig; \
    test "$(ldconfig -p | awk \
        '/libwayland-client.so.0/{print $NF; exit}')" = \
        /usr/local/lib/libwayland-client.so.0


# setup keys
RUN set -eux; \
       key='4B63CF8FDE49746E98FA01DDAD19BAB3CBF125EA'; \
       export GNUPGHOME="$(mktemp -d)"; \
       gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
       mkdir -p /usr/share/keyrings; \
       gpg --batch --export "$key" > /usr/share/keyrings/ros1-snapshots-archive-keyring.gpg; \
       gpgconf --kill all; \
       rm -rf "$GNUPGHOME"

# setup sources.list
RUN echo "deb [ signed-by=/usr/share/keyrings/ros1-snapshots-archive-keyring.gpg ] http://snapshots.ros.org/noetic/final/ubuntu focal main" > /etc/apt/sources.list.d/ros1-snapshots.list

# setup environment
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

ENV ROS_DISTRO=noetic

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-core=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*

# setup entrypoint
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
