#!/usr/bin/env python

import sys
from launchpadlib.launchpad import Launchpad

__DEBUG__ = False
DISTRO = 'ubuntu'
RELEASE = 'trusty'
ARCHITECTURE = 'amd64'
DISTRO_ARCH_SERIES_URL = 'https://api.launchpad.net/1.0/' + DISTRO + '/' + RELEASE + '/' + ARCHITECTURE

## TODO: Accept multiple app names and get all their versions line per line
def get_ppa_archive(launchpad, ppa_url):
  (prefix, rest_ppa_url) = str.split(ppa_url, ':')
  (owner_name, package_name) = str.split(rest_ppa_url, '/')
  owner = launchpad.people[owner_name]
  return owner.getPPAByName(name = package_name)

def get_distro_archive(launchpad, distro_name = DISTRO):
  distro = launchpad.distributions[distro_name]
  return distro.main_archive

def get_latest_package(archive, app_name, distro_url = DISTRO_ARCH_SERIES_URL):
  binaries = archive.getPublishedBinaries(
    status = 'Published',
    exact_match = True,
    binary_name = app_name,
    distro_arch_series = distro_url
  )

  if len(binaries) == 0:
    print("No entries found for app: " + sys.argv[1] + " in archive: " + str(archive))
    sys.exit(1)
  elif __DEBUG__ == True:
    print("Found " + str(len(binaries)) + " matches")
    for sources in binaries:
      print(str(sources.display_name))

  return binaries[0]

def parse_args():
  if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <app name>  [ppa url]")
    print("Example: " + sys.argv[0] + " solaar ppa:daniel.pavel/solaar")
    sys.exit(1)

  app_name = sys.argv[1]
  ppa_url = None
  if len(sys.argv) > 2:
    ppa_url = sys.argv[2]

  return [app_name, ppa_url]

def print_api(obj):
  print(sorted(obj.lp_attributes))
  print(sorted(obj.lp_operations))
  print(sorted(obj.lp_entries))
  print(sorted(obj.lp_collections))

def get_latest_version(app_name, ppa_url):
  launchpad = Launchpad.login_anonymously('launchpad-helper', 'production')
  if ppa_url != None:
    archive = get_ppa_archive(launchpad, ppa_url)
  else:
    archive = get_distro_archive(launchpad)
  package = get_latest_package(archive, app_name)
  return package.binary_package_version

if __name__ == '__main__':
  print(get_latest_version(*parse_args()))
  sys.exit(0)