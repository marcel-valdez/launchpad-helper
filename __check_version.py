#!/usr/bin/env python

import sys

from launchpadlib.launchpad import Launchpad
from __latest_version import get_latest_version
from __latest_version import get_archive

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

def parse_version(version_str):
  version_arr = str.split(version_str, '.')
  major = int(version_arr[0])
  minor = 0
  release = 0
  if len(version_arr) > 1:
    minor = int(version_arr[1])
  if len(version_arr) > 2:
    release = int(str.split(version_arr[2], '-')[0])

  return (major * 100) + (minor * 10) + release

def main(app_name, version, ppa_url):
  archive = get_archive(ppa_url)
  latest_version = get_latest_version(archive, app_name)
  latest = parse_version(str(latest_version))
  current = parse_version(str(version))
  stats = 'current:' + version + ', latest:' + latest_version + ', ' + ppa_url
  if current < latest:
    print app_name + ': out-of-date, ' + stats
  else:
    print app_name + ': up-to-date, ' + stats

if __name__ == '__main__':
  main(*parse_args())
  sys.exit(0)
