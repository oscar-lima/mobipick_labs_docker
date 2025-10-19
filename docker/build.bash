#!/bin/bash

cd focal_snapshot
time docker build -t ozkrelo/focal-snapshot:20250530 . && \
time docker push ozkrelo/focal-snapshot:20250530
cd ..

cd noetic_ros_core
time docker build -t ozkrelo/noetic-ros-core:ubuntu20250530 . && \
time docker push ozkrelo/noetic-ros-core:ubuntu20250530
cd ..

cd mir_robot
time docker build --build-arg ROS_DISTRO=noetic -t ozkrelo/mir:noetic . && \
time docker push ozkrelo/mir:noetic
cd ..

cd mobipick
time docker build --build-arg ROS_DISTRO=noetic -t ozkrelo/mobipick:noetic .
time docker push ozkrelo/mobipick:noetic
cd ..

cd mobipick_labs
time docker build --build-arg ROS_DISTRO=noetic -t ozkrelo/mobipick_labs:noetic .
time docker push ozkrelo/mobipick_labs:noetic
cd ..

# building takes more than 30 minutes on an i7-8550U with fast internet
