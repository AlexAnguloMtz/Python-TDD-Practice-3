from table import Table
from .temperature import Temperature
from .input_validator import InputValidator

class TemperatureConversionReporter:

    def __init__(self):
        self._input_validator = InputValidator()

    def temperature_conversions(self, initial_temperature, final_temperature):
        try:
            return self._do_temperature_conversions(initial_temperature, final_temperature)
        except Exception as exception:
            return str(exception)

    def _do_temperature_conversions(self, initial_temperature, final_temperature):
        self._validate_temperatures(initial_temperature, final_temperature)
        temperatures_table = Table(('Fahrenheit' , 'Celsius'))
        self._add_rows_to_table(temperatures_table, initial_temperature, final_temperature)
        return str(temperatures_table)

    def _add_rows_to_table(self, temperatures_table, initial_temperature, final_temperature):
        for temperature in range(int(initial_temperature), int(final_temperature) + 1):
            self._add_single_row_to_table(temperatures_table, temperature, initial_temperature, final_temperature)

    def _add_single_row_to_table(self, table, temperature, initial_temperature, final_temperature):
        table.add_row(
            self._format_temperature(temperature),
            self._format_temperature(self._convert_to_celsius(temperature))
        )

    def _validate_temperatures(self, initial_temperature, final_temperature):
        self._input_validator.validate_input(initial_temperature, final_temperature)
       
    def _string_contains_integer(self, string):
        return StringUtils.string_contains_integer(string)

    def _convert_to_celsius(self, fahrenheit_temperature):
        return Temperature.convert_to_celsius(fahrenheit_temperature)

    def _format_temperature(self, temperature):
        return f'{temperature:.2f}'