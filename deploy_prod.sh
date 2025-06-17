#!/bin/bash

docker build \
    -t yvideo-admin \
    .
docker run \
    --volume .:/workspaces/yvideo-admin \
    --restart=always
    yvideo-admin
