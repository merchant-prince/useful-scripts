#! /usr/bin/env python3

import os
import argparse
from subprocess import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser("clean-all", description="Clean the system.")
    parser.add_argument("--jetbrains", action="store_true")
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

    # Clean the userspace using Bleachbit

    # Clean the rootspace using Bleachbit

    # Clean pacman & yaourt

    # Clean Jetbrains applications
    if arguments.jetbrains:
        pass

    # Clean the user's home directory (incl. .scripts.d)
