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

def get_latest_source(archive, app_name, distro_url = DISTRO_ARCH_SERIES_URL):
  for series in archive.distribution.series.entries:
    if series['displayname'].lower() == RELEASE.lower():
      distro_series = series['self_link']

  sources = archive.getPublishedSources(
    status = 'Published',
    exact_match = True,
    source_name = app_name,
    distro_series = distro_series
  )


  if len(sources) == 0:
     print("No entries found for app: " + sys.argv[1] + " in archive: " + str(archive))
     sys.exit(1)
  elif __DEBUG__ == True:
    print("Found " + str(len(sources)) + " matches")
    for source in sources:
      print(str(source.display_name))

  return sources[0]

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

  get_url = None
  if len(sys.argv) > 3:
    get_url = sys.argv[3].lower() == "--get_url"

  return { 'app_name': app_name, 'ppa_url': ppa_url, 'get_url': get_url }

def print_api(obj):
  print('lp_attributes: ' + str(sorted(obj.lp_attributes)))
  print('lp_operations: ' + str(sorted(obj.lp_operations)))
  print('lp_entries: ' + str(sorted(obj.lp_entries)))
  print('lp_collections: ' + str(sorted(obj.lp_collections)))

def get_archive(ppa_url):
  launchpad = Launchpad.login_anonymously('launchpad-helper', 'production')
  if ppa_url != None:
    return get_ppa_archive(launchpad, ppa_url)
  else:
    return get_distro_archive(launchpad)

def get_latest_url(archive, app_name):
  return get_latest_source(archive, app_name).binaryFileUrls()[0]

def get_latest_version(archive, app_name):
  return get_latest_source(archive, app_name).source_package_version

if __name__ == '__main__':
  args = parse_args()
  archive = get_archive(args['ppa_url'])
  if args['get_url'] == True:
    print(get_latest_url(archive, args['app_name']))
  else:
    print(get_latest_version(archive, args['app_name']))

  sys.exit(0)
