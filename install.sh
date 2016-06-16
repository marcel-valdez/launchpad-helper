#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -d $HOME/bin ]; then
  mkdir $HOME/bin
fi

cp $SCRIPT_DIR/check-all-versions $HOME/bin
cp $SCRIPT_DIR/__latest_version.py $HOME/bin
cp $SCRIPT_DIR/__check_version.py $HOME/bin
