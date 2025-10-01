#!/usr/bin/env bash

docker build -t sqlite-test:0.1 .
docker run --rm -it --name sqlite-test sqlite-test:0.1 courses.db
