class Color:
    """
    This is a utility class to store the color codes used in the Print
    class.
    """

    # Bright green
    SUCCESS = {
        "HEADER":  "\033[40;38;5;82m",
        "MESSAGE": "\033[30;48;5;82m"
    }

    # Cyan
    INFO = {
        "HEADER":  "\033[40;38;5;4m",
        "MESSAGE": "\033[30;48;5;4m"
    }

    # Yellow
    WARNING = {
        "HEADER":  "\033[40;38;5;220m",
        "MESSAGE": "\033[30;48;5;220m"
    }

    # Bright Red
    ERROR = {
        "HEADER":  "\033[40;38;5;9m",
        "MESSAGE": "\033[30;48;5;9m"
    }

    # Green
    OK = "\033[32m"

    # Red
    FAIL = "\033[91m"

    # Reset color
    RESET = "\033[0m"
