import os
import sys
import datetime
from pathlib import Path
from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.helpers import cd
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, error

try:
    destination = Path(sys.argv[1]).resolve()

    if not destination.exists() or not destination.is_dir():
        raise RuntimeError(f"The specified destination ({destination}) is not an existing directory.")

    HOME = os.getenv("HOME")
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

    print(f"\n{info(f'Backing up data...')}\n\n", end="")

    files = {
        HOME: [
            ".gnupg",
            ".password-store",
            ".ssh",
            ".vimrc",
            ".zshenv",
            ".zshrc"
        ],
        f"{HOME}/Storage": [
            "Documents"
        ]
    }
    password_file_name = "password.txt"

    # export passwords file
    run([f"{root_path}/pass-utils/run.py", "export", f"{destination}/{password_file_name}"], check=True)
    files[str(destination)] = [password_file_name]

    # create archive
    today = datetime.datetime.now().date()
    run(["tar", "-cvzf", f"{destination}/{today.year}_{today.month:02d}_{today.day:02d}.tar.gz",
         *[argument
           for arguments in
           [["-C", parent, *children] for parent, children in files.items()]
           for argument in arguments
           ]
         ],
        check=True)

    os.remove(f"{destination}/{password_file_name}")

    print(f"\n{success(f'Successfully successfully backed up data to {destination}.')}\n\n", end="")

except Exception as exception:
    print(f"\n{error(exception)}\n", end="")
