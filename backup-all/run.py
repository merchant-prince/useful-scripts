#! /usr/bin/env python3

import os
import argparse
from subprocess import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser("backup-all", description="Backup files to a specified directory.")
    parser.add_argument("destination", help="The destination path of the backup archive.")
    arguments = parser.parse_args()

    root_path = os.path.abspath(os.path.dirname(__file__))
    env_path = f"{root_path}/.env"

    # setup venv
    if not os.path.isdir(env_path):
        run(["python3", "-m", "venv", env_path], check=True)

        dependencies = [
            ["--upgrade", "pip"],
            ["harivansh-scripting-utilities"]
        ]

        for dependency in dependencies:
            run([f"{env_path}/bin/pip3", "install", *dependency], check=True)

    env_python3 = f"{env_path}/bin/python3"

    run([env_python3, f"{root_path}/src/backup-all.py", arguments.destination], check=True)
