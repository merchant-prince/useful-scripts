from .Color import Color

class Print:
    """
    This class is used to pretty-print messages
    """

    @staticmethod
    def success(message):
        """Prints a coloured success message"""

        print(Print.__line(Color.SUCCESS['HEADER'], "Success", Color.SUCCESS['MESSAGE'], message), end='')

    @staticmethod
    def info(message):
        """Prints a coloured info message"""

        print(Print.__line(Color.INFO['HEADER'], "Info", Color.INFO['MESSAGE'], message), end='')

    @staticmethod
    def warning(message):
        """Prints a coloured warning message"""

        print(Print.__line(Color.WARNING['HEADER'], "Warning", Color.WARNING['MESSAGE'], message), end='')

    @staticmethod
    def error(message):
        """Prints a coloured error message"""

        print(Print.__line(Color.ERROR['HEADER'], "Error", Color.ERROR['MESSAGE'], message), end='')

    @staticmethod
    def ok():
        """Prints a coloured ok message"""

        print(f"{Color.OK} ...Ok {Color.RESET}", end='')

    @staticmethod
    def fail():
        """Prints a coloured ok message"""

        print(f"{Color.FAIL} ...Failed {Color.RESET}", end='')

    @staticmethod
    def eol(count=1):
        """Prints an end of line character"""

        print('\n' * count, end='')

    @staticmethod
    def __header(color, header):
        """Returns a pretty-string of the header"""

        return f"{color} {header}: {Color.RESET}"

    @staticmethod
    def __message(color, message):
        """Returns a pretty-string of the message"""

        return f"{color}\ue0b0 {message} {Color.RESET}"

    @staticmethod
    def __line(headerColor, header, messageColor, message):
        """Returns a pretified line"""

        return f"{Print.__header(headerColor, header)}{Print.__message(messageColor, message)}"
