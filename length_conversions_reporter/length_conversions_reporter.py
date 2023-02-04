from table import Table
from .length_conversor import LengthConversor
from .input_validator import InputValidator

class LengthConversionsReporter:

    def __init__(self):
        self._input_validator = InputValidator()
    
    def meters_to_english_units(self, initial_meters, final_meters):
        try:
            return self._do_convert_meters_to_english_units(initial_meters, final_meters)
        except Exception as exception:
            return str(exception)

    def _do_convert_meters_to_english_units(self, initial_meters, final_meters):
        self._validate_input(initial_meters, final_meters)
        table = Table(('Meters', 'Yards', 'Feet', 'Inches'))
        for meters in range(int(initial_meters), int(final_meters) + 1):
            self._add_table_row(table, meters, initial_meters, final_meters)
        return str(table)

    def _add_table_row(self, table, meters, initial_meters, final_meters):
        table.add_row(
            meters,
            self._format_result(LengthConversor.meters_to_yards(meters)),
            self._format_result(LengthConversor.meters_to_feet(meters)),
            self._format_result(LengthConversor.meters_to_inches(meters))
        )

    def _format_result(self, result):
        return f'{result:.2f}'

    def _string_contains_integer(self, string):
        return StringUtils.string_contains_integer(string)

    def _validate_input(self, initial_meters, final_meters):
        self._input_validator.validate_input(initial_meters, final_meters)