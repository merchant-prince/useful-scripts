# Useful Scripts

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/merchant-prince/useful-scripts?sort=semver&style=flat-square)

This repository contains scripts to automate some frequent tasks.

## Scripts

The following scripts are available:

### Laravel

This script pulls a [Laravel](https://laravel.com) project in the current working directory and sets up the environment
needed to run the project.
[Docker](https://www.docker.com) is used as the containerization solution for the various services of the generated
project.

#### Usage

```sh
./laravel/run.py    # setup a new laravel project.
```

### Docker Utils

This script allows you to view, edit, and remove the various [Docker](https://www.docker.com) entities present on the
machine.

#### Usage

```sh
./docker-utils/run.py status  # view the docker entities present on the machine.

./docker-utils/run.py purge   # remove all the docker entities present on the machine.

./docker-utils/run.py ui      # start a portainer application at http://localhost:9000.
```

### Pass Utils

This script allows you to import or export passwords present on ```pass```.

#### Usage

```sh
./pass-utils/run.py import passwords.txt  # import passwords from the previously exported password file passwords.txt.

./pass-utils/run.py export passwords.txt  # export passwords to a new passwords file named passwords.txt.
```

### Upgrade All

This script upgrades the entire system.

#### Usage

```sh
./upgrade-all/run.py # upgrade the system.
```

### Clean All

This script cleans the system.

#### Usage

```sh
./clean-all/run.py              # clean the system.
./clean-all/run.py --jetbrains  # clean the system AND jetbrains applications.
```

### Backup All

This script backs up several files and directories.

#### Usage

```sh
./backup-all/run.py .   # backup the files, and save the archive in the current directory.
```

## Updating dependencies

If the dependencies of the project have been updated, remove the **.env** directories from the script directories.
They will be recreated the next time the scripts are run.

```sh
rm -rf ./*/.env
```
