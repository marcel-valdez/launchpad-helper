#!/usr/bin/env python

import sys

from launchpadlib.launchpad import Launchpad
from latest_version import get_latest_version

def parse_args():
  if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <app name>  <current version> [ppa url]")
    print("Example: " + sys.argv[0] + " solaar 0.8.9 ppa:daniel.pavel/solaar")
    sys.exit(1)

  app_name = sys.argv[1]
  version = sys.argv[2]
  ppa_url = None
  if len(sys.argv) > 3:
    ppa_url = sys.argv[3]

  return [app_name, version, ppa_url]

def main(app_name, version, ppa_url):
  print(get_latest_version(app_name, ppa_url))

if __name__ == '__main__':
  main(*parse_args())
  sys.exit(0)
