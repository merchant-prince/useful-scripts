#! /usr/bin/env python3

import os
import sys
import time
import shutil
import argparse
from subprocess import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser("docker-utils",
                                     description="A script to view, manipulate, or purge Docker entities.")
    parser.add_argument("action",
                        choices=("ui", "status", "purge"),
                        help="The action to be carried out by the script.")
    arguments = parser.parse_args()

    root_path = os.path.abspath(os.path.dirname(__file__))
    env_path = f"{root_path}/.env"
    MAX_CACHE_SECONDS = 30 * 60

    if os.path.isdir(env_path) and (time.time() - os.path.getatime(env_path) > MAX_CACHE_SECONDS):
        shutil.rmtree(env_path)

    if not os.path.isdir(env_path):
        run(["python3", "-m", "venv", env_path], check=True)

        dependencies = [
            ["--upgrade", "pip"],
            ["harivansh-scripting-utilities"],
            ["docker"]
        ]

        for dependency in dependencies:
            run([f"{env_path}/bin/pip3", "install", *dependency], check=True)

    env_python3 = f"{env_path}/bin/python3"

    if arguments.action == "ui":
        run([env_python3, f"{root_path}/ui.py"], check=True)

    elif arguments.action == "status":
        run([env_python3, f"{root_path}/status.py"], check=True)

    elif arguments.action == "purge":
        run([env_python3, f"{root_path}/purge.py"], check=True)

    else:
        parser.print_help()
        sys.exit(1)
