import os
import sys
from subprocess import Popen, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, error

password_filepath = sys.argv[1]

if not os.path.isfile(password_filepath):
    print(f"\n{error(f'The file: {password_filepath} does not exist.')}\n\n", end="")

print(f"\n{info(f'Importing passwords...')}\n\n", end="")

with open(password_filepath) as password_file:
    credentials = (tuple(token.strip() for token in item.split()) for item in password_file.read().splitlines())

    for username, password in credentials:
        with Popen(["pass", "insert", "--echo", username], stdin=PIPE) as process:
            process.communicate(input=password.encode("utf-8"))

print(f"\n{success(f'Successfully imported the passwords from {password_filepath}.')}\n\n", end="")
