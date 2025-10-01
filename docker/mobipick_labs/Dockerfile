FROM brean/mobipick:noetic

ENV CATKIN_WS=/root/catkin_ws
ENV CATKIN_WS_SRC=${CATKIN_WS}/src
ARG DEBIAN_FRONTEND=noninteractive

# remove stale ROS list to allow apt to run, then add fresh keyring and source
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

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        python3-pip python3-pyassimp libespeak-dev \
        espeak-data libespeak1 libportaudio2 libsonic0 \
        python3-pydot ros-noetic-qt-dotgraph \
        ros-noetic-rqt-graph \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# TODO: maybe not the best idea to run the default install-deps scripts,
# it might already include some stuff already installed in the mobipick-image?!
RUN cd ${CATKIN_WS_SRC} \
  && git clone https://github.com/dfki-ni/mobipick_labs.git \
  && . ${CATKIN_WS}/devel/setup.sh \
  && cd mobipick_labs \
  && ./install-deps.sh \
  && ./build.sh \
  && rm -rf /var/lib/apt/lists/*
