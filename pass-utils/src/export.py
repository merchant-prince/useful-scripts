import os
import sys
from pathlib import Path
from subprocess import run, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, error

export_filepath = sys.argv[1]
password_store = f"{os.getenv('HOME')}/.password-store"

if os.path.isfile(export_filepath):
    print(f"\n{error(f'The file: {export_filepath} exists. Delete the file, or provide another filename.')}\n\n",
          end="")

print(f"\n{info(f'Exporting passwords...')}\n\n", end="")

credentials = dict((os.path.splitext(path.absolute())[0].replace(f"{password_store}/", "", 1), None)
                   for path in Path(password_store).rglob("*.gpg"))

for username in credentials:
    credentials[username] = run(["pass", username], stdout=PIPE).stdout.decode("utf-8").strip()

with open(export_filepath, "w") as password_file:
    for username, password in credentials.items():
        password_file.write(f"{username} {password}\n")

print(f"\n{success(f'Successfully exported the passwords to {export_filepath}.')}\n\n", end="")
