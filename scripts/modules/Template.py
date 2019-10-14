from string import Template as StringTemplate


class Template:
    """
    A class to process string templates

    Attributes
    ----------
    templatePath:
        The path of the template to read
    templateContent:
        The content of the template after replacing the variables
    """

    def __init__(self, templatePath):
        self.templatePath = templatePath
        self.templateContent = None


    def replace(self, variables):
        """
        Replace the variables in the template (denoted by $) with the variables
        present in the variables dictionary

        Arguments
        ---------
        variables:
            A dictionary containing the variables to be replaced in the
            template
        """

        with open(self.templatePath) as template:
            self.templateContent = StringTemplate(template.read()).safe_substitute(variables)


    def write(self, filename):
        """
        Write the content of the template to the file specified by filename

        Arguments
        ---------
        filename:
            The name of the file in which the content of the template will be
            written
        """

        with open(filename, "w") as file:
            file.write(str(self))


    def __str__(self):
        return self.templateContent
