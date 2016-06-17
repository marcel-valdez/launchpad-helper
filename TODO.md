Features for the future
-----------------------

+ Make the default configuration file for the package configurations be .packages.config
+ Add parameter to check-all-versions to tell it to only display out-of-date packages
+ Make the install.sh script output the things it is doing (copying to $HOME/bin)
+ Give the install.sh script an optional parameter to tell it where to install itself
  + This requires us to output the installation folder to .packages.config, so that uninstall.sh knows where to go to delete files
