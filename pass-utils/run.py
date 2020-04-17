#! /usr/bin/env python3

import os
import sys
import argparse
from subprocess import run

if __name__ == "__main__":
    parser = argparse.ArgumentParser("pass-utils",
                                     description="Import and export pass passwords through cleartext files.")
    subparsers = parser.add_subparsers(help="Actions", dest="action")

    importer = subparsers.add_parser("import", help="Import pass passwords from a text file.")
    importer.add_argument("password_file",
                          help="The path to the cleartext password file from which to import the passwords.")

    exporter = subparsers.add_parser("export", help="Export pass passwords to a text file.")
    exporter.add_argument("password_file",
                          help="The name of the file to which to export the passwords in cleartext.")

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

    if arguments.action == "import":
        filepath = os.path.abspath(arguments.password_file)

        run([env_python3, f"{root_path}/src/import.py", filepath])

    elif arguments.action == "export":
        filepath = os.path.abspath(arguments.password_file)

        run([env_python3, f"{root_path}/src/export.py", filepath])

    else:
        parser.print_help()
        sys.exit(1)
