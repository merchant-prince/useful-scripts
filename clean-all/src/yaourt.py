from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, warning

print(f"\n{warning('** Cleaning Yaourt **')}\n", end="")

# Remove orphans
print(f"\n{info('Removing orphans')}\n", end="")
run(["yaourt", "-Qdtq"])

print(f"\n{success('** Successfully cleaned Yaourt **')}\n", end="")
