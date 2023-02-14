#!/bin/bash

echo "Starting VSCode Server..."

exec /app/openvscode-server/bin/openvscode-server --host 0.0.0.0 --port 7860 --without-connection-token \"${@}\" --
