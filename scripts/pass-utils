#! /usr/bin/env python3


import os
import argparse
from subprocess import Popen, PIPE

from modules.Print import Print


class Import:
    """
    A class for importing credentials from a cleartext file.
    """

    def fromFile(self, filepath):
        """
        Import the credentials into pass from a cleartext file.

        Arguments:
        ----------

        filepath: string
            The path to the file which contains the credentials
            (exported from pass).

            e.g.: /home/foo/bar/PASSWORD_FILE.bak
        """

        if not os.path.isfile(filepath):
            raise RuntimeError(f"The file at {filepath} does not exist.")

        with open(filepath) as passwordFile:
            credentials = dict([tuple(item.split()) for item in passwordFile.read().splitlines()])

        for path, password in credentials.items():
            with Popen(["pass", "insert", "--echo", path], stdin=PIPE) as process:
                process.communicate(input=password.encode("utf-8"))


class Export:
    """
    A class for exporting credentials from pass to a cleartext file.
    """

    def __init__(self):
        self.passwordStorePath = f"{os.getenv('HOME')}/.password-store"
        self.gpgFileExtension = ".gpg"

    def getGpgFilesPath(self):
        """Get an array of all the GPG files"""

        return [path.lstrip(self.passwordStorePath).rstrip(f"{self.gpgFileExtension}\n")
                for path in
                    Popen(["find", self.passwordStorePath, "-name", f"*{self.gpgFileExtension}"],
                          stdout=PIPE,
                          bufsize=1,
                          universal_newlines=True).stdout]

    def getPassword(self, path):
        """
        Get the password of the associated path from pass

        Arguments:
        ----------

        path: string
            The password's path in pass
            e.g.: Foo/Bar/username/password

        Return: string
        -------
        """

        return [password.strip() for password in Popen(["pass", path],
                                                       stdout=PIPE,
                                                       bufsize=1,
                                                       universal_newlines=True).stdout][0]

    def getCredentials(self):
        """
        Get the credentials from pass in the form of {"username": "password", ...}

        Return: dictionary<string:string>
        -------
        """

        return {path:self.getPassword(path) for path in self.getGpgFilesPath()}

    def toFile(self, filepath):
        """
        The path to the file which will contain the credentials in cleartext.

        Arguments:
        ----------

        filepath: string
            The path to the file

            e.g.: /home/foo/bar/PASSWORD_FILE.bak
        """

        if os.path.isfile(filepath):
            raise RuntimeError(f"Another password file exists at: {self.passwordFilePath}. Please delete it before continuing")

        with open(filepath, "w") as passwordFile:
            for path, password in self.getCredentials().items():
                passwordFile.write(f"{path} {password}\n")


class Pass:
    """
    A convenience meta-class to encapsulate the import, and export
    functionality.
    """

    def __init__(self, filepath):
        self.importer = Import()
        self.exporter = Export()
        self.filepath = filepath

    def importPasswords(self):
        self.importer.fromFile(self.filepath)

    def exportPasswords(self):
        self.exporter.toFile(self.filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to import, and export pass's passwords through cleartext files.")

    parser.add_argument("action", choices=["import", "export"], help="The action to be carried out by the script.")
    parser.add_argument("--filepath", default=f"{os.getenv('HOME')}/Downloads/PASSWORD_FILE.bak", help="The full-path of the file to import passwords from, or export passwords to.")

    arguments = parser.parse_args()

    pass_ = Pass(arguments.filepath)

    if arguments.action == "import":
        Print.eol()
        Print.info(f"Importing passwords from: {arguments.filepath}")
        Print.eol(2)

        pass_.importPasswords()

        Print.eol(2)
        Print.success(f"Passwords imported from: {arguments.filepath}")
        Print.eol(2)

    elif arguments.action == "export":
        Print.eol()
        Print.info(f"Exporting passwords to: {arguments.filepath}")

        pass_.exportPasswords()

        Print.eol(2)
        Print.success(f"Passwords saved to: {arguments.filepath}")
        Print.eol(2)
