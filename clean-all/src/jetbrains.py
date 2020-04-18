import re
import os
import shutil
from pathlib import Path
# noinspection PyUnresolvedReferences
from harivansh_scripting_utilities.print import success, warning, error

print(f"\n{warning('** Cleaning Jetbrains application configurations **')}\n", end="")

try:
    directories = {
        os.getenv("HOME"): [
            ".cache/JetBrains",
            ".config/JetBrains",
            ".java",
            ".local/share/JetBrains",
            ".PhpStorm*",
        ]
    }
    paths = []

    for parent_directory, child_directories in directories.items():
        for child_directory in child_directories:
            directory = list(Path(parent_directory).glob(child_directory))[0]
            expected = f"{parent_directory}/{child_directory}"
            actual = str(directory.absolute())

            if expected != actual and re.search(re.escape("*"), child_directory) is None:
                raise RuntimeError(f"Unexpected directory match (expected: [{expected}] actual: [{actual}]).")

            paths.append(directory)

    for path in paths:
        if path.exists() and path.is_dir():
            shutil.rmtree(str(path.absolute()))

    print(f"\n{success('** Successfully cleaned Jetbrains application configurations **')}\n", end="")
except Exception as exception:
    print(f"\n{error(exception)}\n", end="")
