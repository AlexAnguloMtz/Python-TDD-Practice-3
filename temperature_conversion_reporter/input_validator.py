from utils import StringUtils
from .temperature import Temperature

class InputValidator:

    def validate_input(self, initial_temperature, final_temperature):
        if (not StringUtils.all_truthy((initial_temperature, final_temperature))):
            raise ValueError('Cannot process empty temperature. Restart the app.')

        if (not StringUtils.all_contain_integers((initial_temperature, final_temperature))):
            raise TypeError('Temperatures should be integer values. Restart the app.')

        if (not all(map(lambda temperature: self._is_valid_Fahrenheit(int(temperature)), (initial_temperature, final_temperature)))):
            raise ValueError('Cannot continue because temperature is less than absolute zero in Farenheit. Restart the app.')

        if (not (int(initial_temperature) < int(final_temperature))):
            raise ValueError('Initial temperature must be a smaller number than final temperature. Restart the app.')

    def _is_valid_Fahrenheit(self, temperature):
        return Temperature.is_valid_Fahrenheit(temperature)