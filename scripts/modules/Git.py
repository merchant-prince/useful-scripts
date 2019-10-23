from subprocess import run


class Git:
    """
    A class to encapsulate the most common git-based tasks when creating a new
    project
    """
    @staticmethod
    def init():
        run(["git", "init"])
        run(["git", "add", "."])
        run(["git", "commit", "-m", "initial commit"])
        run(["git", "checkout", "-b", "development"])
