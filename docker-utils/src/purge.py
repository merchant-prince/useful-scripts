from subprocess import run, PIPE
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import warning

# Containers
containers = [container.strip() for container in
              run(["docker", "container", "ls", "--all", "--quiet"], stdout=PIPE).stdout.decode("utf-8").split()]

print(f"\n{warning('** STOPPING ALL CONTAINERS **')}\n", end="")
for container in containers:
    run(["docker", "container", "stop", container])

print(f"\n{warning('** REMOVING ALL CONTAINERS **')}\n", end="")
for container in containers:
    run(["docker", "container", "rm", "--force", container])

# Volumes
volumes = [volume.strip() for volume in
           run(["docker", "volume", "ls", "--quiet"], stdout=PIPE).stdout.decode("utf-8").split()]

print(f"\n{warning('** REMOVING ALL VOLUMES **')}\n", end="")
for volume in volumes:
    run(["docker", "volume", "rm", "--force", volume])

# Images
print(f"\n{warning('** REMOVING ALL IMAGES **')}\n", end="")
images = [image.strip() for image in
          run(["docker", "image", "ls", "--all", "--quiet"], stdout=PIPE).stdout.decode("utf-8").split()]

for image in images:
    run(["docker", "image", "rm", "--force", image])

# Networks
print(f"\n{warning('** REMOVING ALL NETWORKS **')}\n", end="")
networks = [network.strip() for network in
            run(["docker", "network", "ls", "--quiet"], stdout=PIPE).stdout.decode("utf-8").split()]

for network in networks:
    run(["docker", "network", "rm", network])
