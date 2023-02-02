from .temperature import Temperature
from table import Table
from utils import StringUtils

class TemperatureConversionReporter:

    def temperature_conversions(self, initial_temperature, final_temperature):
        try:
            return self._do_temperature_conversions(initial_temperature, final_temperature)
        except Exception as exception:
            return str(exception)

    def _do_temperature_conversions(self, initial_temperature, final_temperature):
        self._validate_temperatures(initial_temperature, final_temperature)
        temperatures_table = Table(('Fahrenheit' , 'Celsius'))
        for temperature in range(int(initial_temperature), int(final_temperature) + 1):
            self._add_row(temperatures_table, temperature, initial_temperature, final_temperature)
        return str(temperatures_table)

    def _add_row(self, table, temperature, initial_temperature, final_temperature):
        table.add_row(
            self._format_temperature(temperature),
            self._format_temperature(self._convert_to_celsius(temperature))
        )

    def _validate_temperatures(self, initial_temperature, final_temperature):
        if (not StringUtils.all_truthy((initial_temperature, final_temperature))):
            raise ValueError('Cannot process empty temperature. Restart the app.')

        if (not StringUtils.all_contain_integers((initial_temperature, final_temperature))):
            raise TypeError('Temperatures should be integer values. Restart the app.')

        if (not all(map(lambda temperature: self._is_valid_Fahrenheit(int(temperature)), (initial_temperature, final_temperature)))):
            raise ValueError('Cannot continue because temperature is less than absolute zero in Farenheit. Restart the app.')

        if (not (int(initial_temperature) < int(final_temperature))):
            raise ValueError('Initial temperature must be a smaller number than final temperature. Restart the app.')

    def _string_contains_integer(self, string):
        return StringUtils.string_contains_integer(string)

    def _is_valid_Fahrenheit(self, temperature):
        return Temperature.is_valid_Fahrenheit(temperature)

    def _convert_to_celsius(self, fahrenheit_temperature):
        return Temperature.convert_to_celsius(fahrenheit_temperature)

    def _format_temperature(self, temperature):
        return f'{temperature:.2f}'