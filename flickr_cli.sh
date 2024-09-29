#!/usr/bin/env bash
cd $(dirname $0)
set -e
PYTHON_COMMAND="python3"

if ! command -v python3 &>/dev/null; then
    if ! command -v python &>/dev/null; then
        echo "Error: Python not found, please install python 3.8 or higher and try again"
        exit 1
    fi
fi

if command -v python &>/dev/null; then
   PYTHON_COMMAND="python"
fi

python_version=$($PYTHON_COMMAND --version 2>&1 | awk '{print $2}')  

BASEDIR=$(pwd)
source "$BASEDIR/env/bin/activate"
$PYTHON_COMMAND src/app.py $@
