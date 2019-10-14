class Color:
    """
    This is a utility class to store the color codes used in the Print
    class.
    """

    CODE = {
            "RED_SINDOOR": 9,
            "CHARTREUSE": 82,
            "CYAN": 4,
            "YELLOW": 220,
            "RESET": 0
    }

    def __create(self, colorCode):
        CSI = "\033["
        END = "m"

        return f"{CSI}{colorCode}{END}"

    def __message(self, colorCode):
        FOREGROUND = "40;38;5"

        return f"{FOREGROUND};{colorCode}"

    def __banner(self, colorCode):
        BACKGROUND = "30;48;5"

        return f"{BACKGROUND};{colorCode}"

    def __getattr__(self, name):
        tokens = name.split("_")

        if len(tokens) == 1:
            if tokens[0] == "RESET":
                return self.__create(Color.CODE["RESET"])
            else:
                raise ValueError(f"{name} is not a valid attribute")

        elif len(tokens) == 2:
            colorType, displayType = tokens

            if displayType == "BANNER":
                if colorType == "SUCCESS":
                    return self.__create(self.__banner(Color.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self.__create(self.__banner(Color.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self.__create(self.__banner(Color.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self.__create(self.__banner(Color.CODE["RED_SINDOOR"]))

                else:
                    raise ValueError(f"{name} is not a valid attribute")

            elif displayType == "MESSAGE":
                if colorType == "SUCCESS":
                    return self.__create(self.__message(Color.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self.__create(self.__message(Color.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self.__create(self.__message(Color.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self.__create(self.__message(Color.CODE["RED_SINDOOR"]))

                else:
                    raise ValueError(f"{name} is not a valid attribute")

            else:
                raise ValueError(f"{name} is not a valid attribute")

        else:
            raise ValueError(f"{name} is not a valid attribute")
