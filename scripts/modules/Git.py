from subprocess import run


class Git:
    @staticmethod
    def init():
        run(["git", "init"])
        run(["git", "add", "."])
        run(["git", "commit", "-m", "initial commit"])
        run(["git", "checkout", "-b", "development"])
