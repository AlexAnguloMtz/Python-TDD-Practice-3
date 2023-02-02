class Temperature:

    _FAHRENHEIT_ABSOLUTE_ZERO = -459.67 

    @staticmethod
    def is_valid_Fahrenheit(temperature):
        return temperature >= Temperature._FAHRENHEIT_ABSOLUTE_ZERO

    @staticmethod
    def convert_to_celsius(fahrenheit_temperature):
        return ((fahrenheit_temperature - 32) * 5) / 9