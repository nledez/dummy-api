#!/usr/bin/env bash
if [ -z $BIND_HOST ]; then
	BIND_HOST=127.0.0.1
fi
if [ -z $BIND_PORT ]; then
	BIND_PORT=5000
fi
curl -v ${BIND_HOST}:${BIND_PORT}
