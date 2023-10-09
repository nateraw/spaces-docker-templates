#!/bin/bash

# echo "Starting VSCode Server..."
# exec /app/openvscode-server/bin/openvscode-server --host 0.0.0.0 --port 7860 --without-connection-token \"${@}\" --

echo "Downloading and starting the VSCode server"
# TODO: Put this into the user directory instead of tmp
# TODO: How to determine the name of the HF Space?
mkdir -p ~/vscode
trap '~/vscode/code tunnel unregister' EXIT
cd ~/vscode && curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
tar -xf vscode_cli.tar.gz
~/vscode/code tunnel --accept-server-license-terms --no-sleep --name hf-space-dev-01
