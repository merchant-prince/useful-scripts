from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import info

# Containers
print(f"\n{info('** CONTAINERS **')}\n\n", end="")
run(["docker", "container", "ls", "--all"])

# Volumes
print(f"\n{info('** VOLUMES **')}\n\n", end="")
run(["docker", "volume", "ls"])

# Images
print(f"\n{info('** IMAGES **')}\n\n", end="")
run(["docker", "image", "ls", "--all"])

# Networks
print(f"\n{info('** NETWORKS **')}\n\n", end="")
run(["docker", "network", "ls"])
