from table import Table
from .currency import Currency, InvalidCurrencyException
from .calendar import Calendar
from .input_validator import InputValidator

class RateReporter:

    def __init__(self):
        self._monthly_increment_percentage = 0
        self._initial_rate = 0
        self._currency = 'USD'
        self._input_validator = InputValidator()

    def calculate_yearly_rates(self, initial_year, final_year, month):
        try:
            return self._do_calculate_yearly_rates(initial_year, final_year, month)
        except Exception as exception:
            return str(exception)

    @property
    def monthly_increment_percentage(self):
        return self._monthly_increment_percentage

    @monthly_increment_percentage.setter
    def monthly_increment_percentage(self, value):
        if (value <= 0):
            raise ValueError('Monthly increment percentage must be positive')

        self._monthly_increment_percentage = value
    
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        if (not self._is_valid_currency(currency)):
            raise InvalidCurrencyException(f'Invalid currency: {currency}')

        self._currency = currency

    @property
    def initial_rate(self):
        return self._initial_rate

    @initial_rate.setter
    def initial_rate(self, value):
        if (value <= 0):
            raise ValueError('Initial rate must be positive')

        self._initial_rate = value

    def _do_calculate_yearly_rates(self, initial_year, final_year, month):
        self._validate_input(initial_year, final_year, month)
        table = Table(('Year', 'Month', 'Rate', 'Currency'))
        for year in range(initial_year, final_year + 1):
            self._add_row(table, year, initial_year, month)
        return str(table)

    def _add_row(self, table, year, initial_year, month):
        table.add_row(
            year,
            month,
            self._format_rate(self._rate_for_year(year, initial_year)),
            self.currency
        )

    def _validate_input(self, initial_year, final_year, month):
        self._input_validator.validate_input(initial_year, final_year, month)
            
    def _rate_for_year(self, year, initial_year):
        rate = self.initial_rate
        for year in range(initial_year, year):
            for month in range(self._months_in_a_year()):
                rate += ((rate * self.monthly_increment_percentage) / 100)
        return rate

    def _months_in_a_year(self):
        return Calendar.months_in_a_year()

    def _format_rate(self, rate):
        return f'{rate:.2f}'

    def _is_valid_currency(self, currency):
        return Currency.is_valid_currency(currency)