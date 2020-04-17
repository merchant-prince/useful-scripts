from subprocess import run, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, warning, error

print(f"\n{warning('** Cleaning Pacman **')}\n", end="")

# Remove orphans
orphans = [orphan.strip() for orphan in run(["pacman", "-Qdtq"], stdout=PIPE).stdout.decode("utf-8").split()]

if orphans:
    print(f"\n{info('** Removing orphans **')}\n", end="")

    try:
        run(["sudo", "pacman", "-Rs", *orphans], check=True)
    except Exception as exception:
        print(f"\n{error(exception)}\n", end="")

# Clear cache
print(f"\n{info('** Clearing cache **')}\n", end="")

try:
    run(["sudo", "pacman", "-Scc"], check=True)
except Exception as exception:
    print(f"\n{error(exception)}\n", end="")

# View pacdiff
print(f"\n{info('** Viewing pacdiff **')}\n", end="")
run(["sudo", "pacdiff"])

print(f"\n{success('** Successfully cleaned Pacman **')}\n", end="")
