#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -d $HOME/bin ]; then
  mkdir $HOME/bin
fi

echo "Copying files to $HOME/bin"
cp --verbose $SCRIPT_DIR/check-all-versions $HOME/bin
cp --verbose $SCRIPT_DIR/__latest_version.py $HOME/bin
cp --verbose $SCRIPT_DIR/__check_version.py $HOME/bin
cp --verbose $SCRIPT_DIR/verify-packages $HOME/bin

echo "Export $HOME/dir to your PATH variable in order to have the"
echo "command line tools available in a terminal"
