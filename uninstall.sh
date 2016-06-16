#!/usr/bin/env bash

CHECK_VERSION="$HOME/bin/__check_version.py"
CHECK_ALL_VERSIONS="$HOME/bin/check-all-versions"
LATEST_VERSION="$HOME/bin/__latest_version.py"


if [ -f $CHECK_ALL_VERSIONS ]; then
  echo "Deleting $CHECK_ALL_VERSIONS"
  rm $CHECK_ALL_VERSIONS
fi

if [ -f $LATEST_VERSION ]; then
  echo "Deleting $LATEST_VERSION"
  rm $LATEST_VERSION
fi

if [ -f $CHECK_VERSION ]; then
  echo "Deleting $CHECK_VERSION"
  rm $CHECK_VERSION
fi
