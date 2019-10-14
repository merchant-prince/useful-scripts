from .Color import Color as ColorClass


Color = ColorClass()


class Print:
    """
    This class is used to pretty-print messages
    """

    @staticmethod
    def success(message):
        """Prints a coloured success message"""

        print(Print.__line(Color.SUCCESS_BANNER, "Success", Color.SUCCESS_MESSAGE, message), end='')


    @staticmethod
    def info(message):
        """Prints a coloured info message"""

        print(Print.__line(Color.INFO_BANNER, "Info", Color.INFO_MESSAGE, message), end='')


    @staticmethod
    def warning(message):
        """Prints a coloured warning message"""

        print(Print.__line(Color.WARNING_BANNER, "Warning", Color.WARNING_MESSAGE, message), end='')


    @staticmethod
    def error(message):
        """Prints a coloured error message"""

        print(Print.__line(Color.ERROR_BANNER, "Error", Color.ERROR_MESSAGE, message), end='')


    @staticmethod
    def ok():
        """Prints a coloured ok message"""

        print(f"{Color.SUCCESS_MESSAGE} ...Ok {Color.RESET}", end='')


    @staticmethod
    def fail():
        """Prints a coloured failure message"""

        print(f"{Color.ERROR_MESSAGE} ...Failed {Color.RESET}", end='')


    @staticmethod
    def eol(count=1):
        """Prints an end of line character"""

        print('\n' * count, end='')


    @staticmethod
    def __line(headerColor, header, messageColor, message):
        """Returns a pretified line"""

        return f"{Print.__header(headerColor, header)}{Print.__message(messageColor, message)}"


    @staticmethod
    def __header(color, header):
        """Returns a pretty-string of the header"""

        return f"{color} {header}: {Color.RESET}"


    @staticmethod
    def __message(color, message):
        """Returns a pretty-string of the message"""

        return f"{color}\ue0b0 {message} {Color.RESET}"
