#!/bin/bash

version=1.2
tag=noetic-v$version

docker build -t ozkrelo/x_mobipick_labs:$tag .
