#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ ! -d "$HOME/bin" ]; then
  echo "No $HOME/bin directory exists, do you wish to create one? [yY]"
  read __answer
  if [ "$__answer" == "y" ] || [ "$__answer" == "Y" ]; then
    mkdir $HOME/bin
    echo "Add PATH entry for $HOME/bin in $PATH"
    echo 'if [ -d $HOME/bin ]; then'
    echo '  export PATH=$PATH:"$HOME/bin"' >> "$HOME/.bashrc"
    echo 'fi'
  fi
fi

if [ ! -d "$HOME/bin" ]; then
  echo "There is no $HOME/bin directory, cannot continue with installation"
fi

echo "Copying files to $HOME/bin"
cp --verbose $SCRIPT_DIR/check-all-versions $HOME/bin
cp --verbose $SCRIPT_DIR/__latest_version.py $HOME/bin
cp --verbose $SCRIPT_DIR/__check_version.py $HOME/bin
cp --verbose $SCRIPT_DIR/verify-packages $HOME/bin
cp --verbose $SCRIPT_DIR/update-package $HOME/bin



echo "Export $HOME/dir to your PATH variable in order to have the"
echo "command line tools available in a terminal."

echo "Do you wish to check for your package versions every computer restart? [yY]"
read __answer

if [ "$__answer" == "y" ] || [ "$__answer" == "Y" ]; then
  echo "verify-packages --use-cache" >> "$HOME/.bashrc"
else
  echo "In order to have the tool check versions every time you restart"
  echo "your computer, you need to add this line to your .bashrc:"
  echo "verify-packages --use-cache"
fi
