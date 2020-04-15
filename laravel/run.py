#! /usr/bin/env python3

import os
import sys
import shutil
import argparse
from subprocess import run


if __name__ == "__main__":
    # Constants
    NEW_PROJECT = "new-project"
    REFRESH_INSTALLER = "refresh-installer"

    # Argument parsing
    parser = argparse.ArgumentParser(description="Setup a new Laravel application.")
    parser.add_argument("action", choices=(NEW_PROJECT, REFRESH_INSTALLER), help="Actions to take on the script.")
    arguments = parser.parse_args()

    env_dirname = ".env"
    script_dirname = os.path.abspath(os.path.dirname(__file__))
    env_dir = f"{script_dirname}/{env_dirname}"
    laravel_installer_package_name = "harivansh_laravel_docker"

    # Setup a new laravel project
    if arguments.action == NEW_PROJECT:
        env_python3 = f"{env_dir}/bin/python3"

        run([env_python3, "-m", laravel_installer_package_name], check=True)

    # Refresh the laravel installer
    elif arguments.action == REFRESH_INSTALLER:
        env_pip3 = f"{env_dir}/bin/pip3"

        if os.path.isdir(env_dir):
            shutil.rmtree(env_dir)

        run(["python3", "-m", "venv", env_dir], check=True)
        run([env_pip3, "install", "--upgrade", "pip"], check=True)

        run([env_pip3, "install", "--upgrade", laravel_installer_package_name], check=True)
    else:
        parser.print_help()
        sys.exit(1)
