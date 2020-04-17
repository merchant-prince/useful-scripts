from subprocess import run, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, warning, error

print(f"\n{warning('** Cleaning the userspace using Bleachbit **')}\n", end="")

try:
    excluded_cleaners = ("system.free_disk_space", "system.memory")
    cleaners = (cleaner.strip() for cleaner in
                run(["bleachbit", "--list-cleaners"], stdout=PIPE, check=True).stdout.decode("utf-8").split()
                if cleaner not in excluded_cleaners)

    run(["bleachbit", "--clean", *cleaners], check=True)

except Exception as exception:
    print(f"\n{error(exception)}\n", end="")

print(f"\n{success('** Successfully cleaned the userspace using Bleachbit **')}\n", end="")
