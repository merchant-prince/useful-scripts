#! /usr/bin/env python3

import os
import shutil
from subprocess import run

if __name__ == "__main__":
    root_path = os.path.abspath(os.path.dirname(__file__))
    env_path = f"{root_path}/.env"

    if os.path.isdir(env_path):
        shutil.rmtree(env_path)

    run(["python3", "-m", "venv", env_path], check=True)

    dependencies = [
        ["--upgrade", "pip"],
        ["harivansh-scripting-utilities"]
    ]

    for dependency in dependencies:
        run([f"{env_path}/bin/pip3", "install", *dependency], check=True)

    run([f"{env_path}/bin/python3", f"{root_path}/src/update-all.py"], check=True)

    shutil.rmtree(env_path)
