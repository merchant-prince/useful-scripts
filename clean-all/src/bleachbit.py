import sys
from subprocess import run, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, warning, error

entity = sys.argv[1]

print(f"\n{warning('** Cleaning the userspace using Bleachbit **')}\n", end="")

try:
    excluded_cleaners = ("system.free_disk_space", "system.memory")
    cleaners = (cleaner.strip() for cleaner in
                run(["bleachbit", "--list-cleaners"], stdout=PIPE, check=True).stdout.decode("utf-8").split()
                if cleaner not in excluded_cleaners)

    command = ["bleachbit", "--clean", *cleaners]

    if entity == "root":
        command.insert(0, "sudo")

    run(command, check=True)

except Exception as exception:
    print(f"\n{error(exception)}\n", end="")

print(f"\n{success('** Successfully cleaned the userspace using Bleachbit **')}\n", end="")
