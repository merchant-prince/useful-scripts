import re
import os

from .Print import Print




def check_project_name(projectName):
    Print.info("Checking project name")

    projectNameIsPascalCased = bool(re.match('^[A-Z][a-z]+(?:[A-Z][a-z]+)*$', projectName))

    if projectNameIsPascalCased:
        Print.ok()
        Print.eol(2)
    else:
        Print.fail()
        Print.eol(2)
        Print.error("The project name is not pascal-cased")
        Print.eol()
        sys.exit(1)


def check_project_existence(projectName):
    Print.info("Checking project existence within current directory")

    projectExists = os.path.isdir(projectName) if projectName in os.listdir() else False

    if not projectExists:
        Print.ok()
        Print.eol(2)
    else:
        Print.fail()
        Print.eol(2)
        Print.error("Another project with the same name already exists in this directory")
        Print.eol()
        sys.exit(1)
