from subprocess import run
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, info, error

try:
    print(f"""\n{info("Refreshing pacman mirrors...")}\n""", end="")
    run(["sudo", "pacman-mirrors", "-f"], check=True)
    print(f"""\n{success("Pacman mirrors have been refreshed.")}\n""", end="")

    print(f"""\n{info("Upgrading pacman packages...")}\n""", end="")
    run(["sudo", "pacman", "-Syyu"], check=True)
    print(f"""\n{success("Pacman packages have been upgraded.")}\n""", end="")

    print(f"""\n{info("Upgrading Arch User Repository (AUR) packages...")}\n""", end="")
    run(["yaourt", "-Syuua"], check=True)
    print(f"""\n{success("Pacman packages have been upgraded.")}\n""", end="")

except Exception as exception:
    print(f"""\n{error(exception)}\n""", end="")
