import os
from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.helpers import cd
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import info, error


print(f"\n{info('** STARTING PORTAINER **')}\n\n", end="")

compose_context = f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/resources/portainer"

with cd(compose_context):
    run(["docker-compose", "up"])
