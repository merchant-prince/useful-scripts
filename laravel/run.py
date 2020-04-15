#! /usr/bin/env python3

import os
import sys
import argparse
from subprocess import run

if __name__ == "__main__":
    SETUP = "setup"

    parser = argparse.ArgumentParser("laravel", description="Setup a new Laravel application.")
    parser.add_argument("action", choices=(SETUP,), help="Actions to take on the script.")
    arguments = parser.parse_args()

    env_dir = f"{os.path.abspath(os.path.dirname(__file__))}/.env"

    # Setup a new laravel project
    if arguments.action == SETUP:
        env_python3 = f"{env_dir}/bin/python3"

        run([env_python3, "-m", "harivansh_laravel_docker"], check=True)
    else:
        parser.print_help()
        sys.exit(1)
