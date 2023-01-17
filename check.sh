#!/bin/bash
curl -v ${BIND_HOST:-127.0.0.1}:${BIND_PORT:-5000}
