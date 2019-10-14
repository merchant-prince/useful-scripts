import re
import os

from .Print import Print


class Check:
    """
    A utility class to perform various checks on a project
    """

    def __init__(self, projectName):
        self.projectName = projectName


    def projectName(self):
        """
        Check the project name
        """

        Print.info("Checking project name")

        projectNameIsPascalCased = bool(re.match('^[A-Z][a-z]+(?:[A-Z][a-z]+)*$', self.projectName))

        if projectNameIsPascalCased:
            Print.ok()
            Print.eol(2)
        else:
            Print.fail()
            Print.eol(2)
            Print.error("The project name is not pascal-cased")
            Print.eol()
            sys.exit(1)


    def projectExistence():
        """
        Check if a project with the same name already exists in the current directory
        """

        Print.info("Checking project existence within current directory")

        projectExists = os.path.isdir(projectName) if self.projectName in os.listdir() else False

        if not projectExists:
            Print.ok()
            Print.eol(2)
        else:
            Print.fail()
            Print.eol(2)
            Print.error("Another project with the same name already exists in this directory")
            Print.eol()
            sys.exit(1)
