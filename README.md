# Git projects automation script

The script keeps track of multiple git repositories. In the script.conf file
the user must put the path to the configuration files for the projects that they
want to keep track. Each project configuration file contains the name of the
project, the command for build, the list of files that are generated after
the build and the list of files that will be moved.

When there is a new version of the project in the repository, the files are
pulled locally and built. The binary files resulted are moved to a new folder
which will contain a subfolder for each build named "Build_N" where N is
incremented automatically.

Each project is owned by a different user and they don't have access to the
other projects. The users are created automatically in the script and they have
the same name as the project they own.
