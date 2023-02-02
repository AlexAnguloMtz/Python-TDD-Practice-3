from utils import StringUtils
from table import Table
from .currency import Currency
from .calendar import Calendar

class RateReporter:

    def __init__(self):
        self._monthly_increment_percentage = 0
        self._initial_rate = 0
        self._currency = 'USD'

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
            raise ValueError(f'Invalid currency: {currency}')

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
        for year in range(int(initial_year), int(final_year) + 1):
            self._add_row(table, year, initial_year, month)
        return str(table)

    def _add_row(self, table, year, initial_year, month):
        table.add_row(
            year,
            month,
            self._format_rate(self._rate_for_year(year, int(initial_year))),
            self.currency
        )

    def _validate_input(self, initial_year, final_year, month):
        if (not StringUtils.all_truthy((initial_year, final_year))):
            raise ValueError('Cannot process empty year')

        if (not StringUtils.all_contain_integers((initial_year, final_year))):
            raise ValueError('Years must be integers')

        if (int(initial_year) > int(final_year)):
            raise ValueError('Initial year cannot be greater than final year')

        if (not self._is_valid_month(month)):
            raise ValueError(f'Invalid month: {month}')
            
    def _string_contains_integer(self, string):
        return StringUtils.string_contains_integer(string)
    
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

    def _is_valid_month(self, month):
        return Calendar.is_valid_month(month)