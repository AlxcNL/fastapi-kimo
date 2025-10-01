# Use an official Python runtime as a parent image
FROM debian:testing-slim

# Install SQLite
RUN apt update && apt install -y sqlite3

WORKDIR /tmp

ADD db .

# App to start when running container
ENTRYPOINT [ "sqlite3" ]
