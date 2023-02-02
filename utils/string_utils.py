from .numbers import Numbers

class StringUtils:

    @staticmethod
    def string_contains_integer(string):
        return (Numbers.is_valid_float(string)) and (not '.' in string)

    @staticmethod
    def all_truthy(strings):
        return all(map((lambda string: True if string else False), strings))

    @staticmethod
    def all_contain_integers(strings):
        return all(map(StringUtils.string_contains_integer, strings))