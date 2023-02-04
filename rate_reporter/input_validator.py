from utils import Numbers
from .calendar import Calendar

class InputValidator:

    def validate_input(self, initial_year, final_year, month):
        if (not Numbers.all_integers(initial_year, final_year)):
            raise ValueError('Years must be integers')

        if (initial_year > final_year):
            raise ValueError('Initial year cannot be greater than final year')

        if (not self._is_valid_month(month)):
            raise ValueError(f'Invalid month: {month}')

    def _is_valid_month(self, month):
        return Calendar.is_valid_month(month)