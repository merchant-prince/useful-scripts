from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, warning, error

print(f"\n{warning('** Cleaning the system **')}\n", end="")

try:
    JOURNALCTL_VACUUM_SIZE = "50M"
    JOURNALCTL_VACUUM_TIME = "30days"

    run(["sudo", "journalctl",
         f"--vacuum-size={JOURNALCTL_VACUUM_SIZE}",
         f"--vacuum-time={JOURNALCTL_VACUUM_TIME}"], check=True)

except Exception as exception:
    print(f"\n{error(exception)}\n", end="")

print(f"\n{success('** Successfully cleaned the system **')}\n", end="")
