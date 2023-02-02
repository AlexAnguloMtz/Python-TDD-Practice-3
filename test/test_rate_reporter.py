import unittest
from rate_reporter import RateReporter

class TestRateReporter(unittest.TestCase):

    def test_should_generate_expected_report(self):

        app = RateReporter()
        app.currency = 'MXN'
        app.initial_rate = 57.00
        app.monthly_increment_percentage = 4

        expected_report = '--------------------------------------' + '\n' + \
                          '| Year | Month   | Rate   | Currency |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 2010 | January | 57.00  | MXN      |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 2011 | January | 91.26  | MXN      |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 2012 | January | 146.11 | MXN      |' + '\n' + \
                          '--------------------------------------' 
        
        self.assertEqual(
            expected_report,
            app.calculate_yearly_rates('2010', '2012', 'January')
        )

    def test_should_keep_track_of_monthly_increment(self):
        app = RateReporter()
        app.monthly_increment_percentage = 4

        self.assertEqual(4, app.monthly_increment_percentage)
    
    def test_should_keep_track_of_currency(self):
        app = RateReporter()
        app.currency = 'MXN'

        self.assertEqual('MXN', app.currency)

    def test_should_return_error_message_for_empty_initial_year(self):
        app = RateReporter()
        self.assertEqual('Cannot process empty year', app.calculate_yearly_rates('', '2023', 'June'))

    def test_should_return_error_message_for_empty_final_year(self):
        app = RateReporter()
        self.assertEqual('Cannot process empty year', app.calculate_yearly_rates('2023', '', 'June'))

    def test_should_return_error_message_if_initial_year_is_after_final_year(self):
        app = RateReporter()
        self.assertEqual('Initial year cannot be greater than final year', app.calculate_yearly_rates('2023', '2020', 'June'))

    def test_should_return_error_message_if_initial_year_is_not_an_integer(self):
        app = RateReporter()
        self.assertEqual('Years must be integers', app.calculate_yearly_rates('Not an integer', '2023', 'June'))

    def test_should_return_error_message_if_final_year_is_not_an_integer(self):
        app = RateReporter()
        self.assertEqual('Years must be integers', app.calculate_yearly_rates('2023', 'Not an integer', 'June'))

    def test_should_return_error_message_for_empty_month(self):
        app = RateReporter()
        self.assertEqual('Invalid month: ', app.calculate_yearly_rates('2020', '2023', ''))

    def test_should_return_error_message_for_invalid_month(self):
        app = RateReporter()
        self.assertEqual('Invalid month: Some month', app.calculate_yearly_rates('2020', '2023', 'Some month'))
    