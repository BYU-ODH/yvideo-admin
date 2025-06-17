FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y curl git && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    source $HOME/.local/bin/env && \
    uv sync

WORKDIR /workspaces/yvideo-admin

CMD uv run --with gunicorn gunicorn --config=./gunicorn.conf.py
