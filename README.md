Launchpad Helper
----------------

## What is it?

Launchpad helper aims to be a set of utility scripts that consume the launchpad.net Web API
in order to perform useful tasks. Launchpad.net is the hostname of the server that manages
Ubuntu's package system (Synaptic Package Manager).

Currently there is only one utility script:

+ check-all-versions: It allows you to keep track of the versions of a set of
  packages listed in a file in a specific format that it understands.


## Utilities

### check-all-versions

#### How do I use it?

You must create a configuration file with the following format:

\<package-name> \<current.known.version> \<ppa:url.of/package>

Example entries:

solaar 0.9.2 ppa:some.author/solaar

albert 0.8.9 ppa:other.author/webupd8

Then you must either export the configuration file path as a variable named `CHECK_PACKAGES_CONFIG`
or specify it as a parameter for the `check-all-versions` script.

Example usage:

```
$ check-all-versions
# optionally pass in the filepath of the configuration file like:
# check-all-versions .configfile
solaar: out-of-date, current:0.9.2, latest:0.9.3, ppa:some.author/solaar
albert: up-to-date, current:0.8.9, latest: 0.8.9-1, ppa:other.author/webupd8
```

#### How does it work?

What the script will do is fetch the latest version from launchpad.net using the specified
PPA url, compare it against the latest uploaded version and display the results for each
entry in the configuraiton file.
