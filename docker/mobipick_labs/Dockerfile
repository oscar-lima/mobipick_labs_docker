FROM brean/mobipick:noetic

ENV CATKIN_WS=/root/catkin_ws
ENV CATKIN_WS_SRC=${CATKIN_WS}/src
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

# use bash for RUN so we can 'source' scripts
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# refresh ROS apt source and base tools
RUN set -eux; \
    rm -f /etc/apt/sources.list.d/ros*.list || true; \
    apt-get update -qq; \
    apt-get install -y --no-install-recommends ca-certificates curl gnupg; \
    curl -fsSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
      | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg; \
    echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros/ubuntu focal main' \
      > /etc/apt/sources.list.d/ros1.list; \
    apt-get update -qq; \
    rm -rf /var/lib/apt/lists/*

# system packages
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        git python3-pip python3-pyassimp libespeak-dev \
        espeak-data libespeak1 libportaudio2 libsonic0 \
        python3-pydot ros-noetic-qt-dotgraph \
        ros-noetic-rqt-graph \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pip compatible with py3.8 and pin scientific stack
RUN python3 -m pip install --upgrade 'pip<25'
RUN python3 -m pip install --upgrade --force-reinstall \
      'numpy==1.24.4' 'scipy==1.10.1' 'ConfigSpace>=0.7.0'

# fetch sources and build (source ROS with nounset disabled briefly)
RUN set -eux; \
  mkdir -p "${CATKIN_WS_SRC}"; \
  cd "${CATKIN_WS_SRC}"; \
  git clone https://github.com/dfki-ni/mobipick_labs.git; \
  export ROS_MASTER_URI=${ROS_MASTER_URI:-http://localhost:11311}; \
  export ROS_HOSTNAME=${ROS_HOSTNAME:-localhost}; \
  export ROS_IP=${ROS_IP:-127.0.0.1}; \
  set +u; source /opt/ros/noetic/setup.bash; set -u; \
  cd mobipick_labs; \
  ./install-deps.sh; \
  ./build.sh
