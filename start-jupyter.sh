#!/bin/bash

docker build --network host --tag htwk-robots:jupyter .

docker run --network host -v $PWD:/mnt/notebooks/ htwk-robots:jupyter


