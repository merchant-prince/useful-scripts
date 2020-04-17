# Useful Scripts

This repository contains scripts to automate some frequent tasks.

## Scripts

The following scripts are available:

### Laravel

This script pulls a [Laravel](https://laravel.com) project in the current working directory and sets up the environment
needed to run the project.
[Docker](https://www.docker.com) is used as the containerization solution for the various services of the generated
project.

#### Usage

To create a new laravel project, call the **run.py** script.

```sh
./laravel/run.py
```

#### Clean

If the dependencies of the project have been updated, remove the **.env** directory.

```sh
rm -rf ./laravel/.env
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

#### Clean

If the dependencies of the project have been updated, remove the **.env** directory.

```sh
rm -rf ./docker-utils/.env
```

### Pass Utils

This script allows you to import or export passwords present on ```pass```.

#### Usage

```sh
./pass-utils/run.py import passwords.txt  # import passwords from the previously exported password file passwords.txt.

./pass-utils/run.py export passwords.txt  # export passwords to a new passwords file named passwords.txt.
```

#### Clean

If the dependencies of the project have been updated, remove the **.env** directory.

```sh
rm -rf ./pass-utils/.env
```

### Update All

This script updates the entire system.

#### Usage

To update the system, run the following command:

```sh
./update-all/run.py
```

#### Clean

If the dependencies of the project have been updated, remove the **.env** directory.

```sh
rm -rf ./update-all/.env
```
