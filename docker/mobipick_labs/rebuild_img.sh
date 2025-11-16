#!/bin/bash

version=1.1
tag=noetic-v$version

docker build -t ozkrelo/mobipick:$tag .
