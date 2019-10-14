import os
import collections

from .cd import cd
from .Print import Print


class DirectoryStructure:
    """
    A class to create a directory structure according to the structure defined.

    Attributes
    ----------
    structure:
        A dictionary of dictionaries representing the directory structure.

        e.g.: { "one": {
                    "eleven": {},
                    "twelve": {}
                },
                "two": {}
              }
    """
    def __init__(self, structure):
        Print.info("Checking directory structure")

        DirectoryStructure.__checkStructure(structure)

        Print.ok()
        Print.eol()

        Print.info("Creating directory structure")

        DirectoryStructure.__createDirectory(structure)

        Print.ok()
        Print.eol()

    @staticmethod
    def __createDirectory(structure):
        for key, value in structure.items():
            os.mkdir(key)

            with cd(key):
                DirectoryStructure.__createDirectory(value)

    @staticmethod
    def __checkStructure(dictionary):
        if not isinstance(dictionary, collections.Mapping):
            raise ValueError("The directory structure provided is ill-formed")

        for key, value in dictionary.items():
            if isinstance(value, collections.Mapping):
                DirectoryStructure.__checkStructure(value)
            else:
                raise ValueError("The directory structure provided is ill-formed")
