# encoding=utf-8
__author__ = 'LoveLYJ'


class TypeError(Exception):
    def __init__(self, variable, ClassType):
        """
        :param variable: 变量名称，str类型
        :param type:     类型，should be this type
        :return:
        """
        self.type = str(ClassType.__name__)
        self.variable = str(variable)

    def __str__(self):
        return repr("[Error]The parameter:[" + self.variable + "] here should be instance of Class:[" + self.type + "]")

class CorpusPathError(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return repr("[Error]path:\"" + self.path + "\" is invalid")