import re
import os


class Check:
    """
    A utility class to perform various checks on a project
    """

    def __init__(self, projectName):
        self.project = {
                "name": projectName
        }


    def nameIsPascalCased(self):
        """
        Check if the project name is PascalCased
        """

        return bool(re.match('^[A-Z][a-z]+(?:[A-Z][a-z]+)*$', self.project["name"]))


    def projectExists(self):
        """
        Check if a project with the same name already exists in the current directory
        """

        return os.path.isdir(project["name"]) if self.project["name"] in os.listdir() else False
