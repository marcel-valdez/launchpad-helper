#!/usr/bin/env bash

function uninstall_file() {
  if [ -f "$1" ]; then
    rm --verbose "$1"
  fi
}

echo "Deleting files from $HOME/bin"
uninstall_file "$HOME/bin/check-all-versions"
uninstall_file "$HOME/bin/__latest_version.py"
uninstall_file "$HOME/bin/__check_version.py"
uninstall_file "$HOME/bin/verify-packages"
uninstall_file "$HOME/bin/update-package"
