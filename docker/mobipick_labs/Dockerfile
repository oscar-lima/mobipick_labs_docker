FROM ozkrelo/mobipick:noetic-v1.1

ENV CATKIN_WS=/root/catkin_ws
ENV CATKIN_WS_SRC=${CATKIN_WS}/src
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
# make pip more robust in Docker to avoid intermittent SSL download errors
# docs: PIP_RETRIES, PIP_DEFAULT_TIMEOUT, PIP_RESUME_RETRIES, PIP_PROGRESS_BAR
ENV PIP_RETRIES=20 \
    PIP_DEFAULT_TIMEOUT=120 \
    PIP_RESUME_RETRIES=20 \
    PIP_PROGRESS_BAR=off

# use bash for RUN so we can 'source' scripts
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# system packages
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
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

# TODO: maybe not the best idea to run the default install-deps scripts,
# it might already include some stuff already installed in the mobipick-image?!
RUN cd ${CATKIN_WS_SRC} \
  && git clone https://github.com/dfki-ni/mobipick_labs.git \
  && . ${CATKIN_WS}/devel/setup.sh \
  && cd mobipick_labs \
  && ./install-deps.sh \
  && ./build.sh \
  && rm -rf /var/lib/apt/lists/*
