import unittest
from temperature_conversion_reporter import TemperatureConversionReporter

class TestTemperatureConversionReporter(unittest.TestCase):

    def test_should_generate_expected_table(self):
        
        app = TemperatureConversionReporter()

        expected_table = '------------------------' + '\n' + \
                         '| Fahrenheit | Celsius |' + '\n' + \
                         '------------------------' + '\n' + \
                         '| 50.00      | 10.00   |' + '\n' + \
                         '------------------------' + '\n' + \
                         '| 51.00      | 10.56   |' + '\n' + \
                         '------------------------' + '\n' + \
                         '| 52.00      | 11.11   |' + '\n' + \
                         '------------------------'

        self.assertEqual(
            expected_table,
            app.temperature_conversions('50', '52')
        )

    def test_should_return_error_message_for_empty_initial_temperature(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Cannot process empty temperature. Restart the app.',
            app.temperature_conversions('', '100')
        )

    def test_should_return_error_message_for_empty_final_temperature(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Cannot process empty temperature. Restart the app.',
            app.temperature_conversions('100', '')
        )

    def test_should_return_error_message_if_initial_temperature_string_is_a_float(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Temperatures should be integer values. Restart the app.',
            app.temperature_conversions('90.100', '100')
        )

    def test_should_return_error_message_if_final_temperature_string_is_a_float(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Temperatures should be integer values. Restart the app.',
            app.temperature_conversions('90', '100.100')
        )

    def test_should_return_error_message_if_initial_temperature_string_is_not_a_number(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Temperatures should be integer values. Restart the app.',
            app.temperature_conversions('Not a number', '100')
        )
 
    def test_should_return_error_message_if_final_temperature_string_is_not_a_number(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Temperatures should be integer values. Restart the app.',
            app.temperature_conversions('100', 'Not a number')
        )

    def test_should_return_error_message_if_initial_temperature_is_less_than_absolute_zero_in_Farenheit(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Cannot continue because temperature is less than absolute zero in Farenheit. Restart the app.',
            app.temperature_conversions(self._Fahrenheit_less_than_absolute_zero(), '100')
        )
    
    def test_should_return_error_message_if_final_temperature_is_less_than_absolute_zero_in_Farenheit(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Cannot continue because temperature is less than absolute zero in Farenheit. Restart the app.',
            app.temperature_conversions('100', self._Fahrenheit_less_than_absolute_zero())
        )

    def test_should_return_error_message_if_initial_temperature_is_greater_than_final_temperature(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Initial temperature must be a smaller number than final temperature. Restart the app.',
            app.temperature_conversions('100', '50')
        )

    def test_should_return_error_message_if_initial_temperature_is_equal_to_final_temperature(self):
        app = TemperatureConversionReporter()
        self.assertEqual(
            'Initial temperature must be a smaller number than final temperature. Restart the app.',
            app.temperature_conversions('50', '50')
        )

    def _Fahrenheit_less_than_absolute_zero(self):
        return '-460'
    

    