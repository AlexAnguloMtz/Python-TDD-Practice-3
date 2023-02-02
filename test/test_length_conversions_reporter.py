import unittest
from length_conversions_reporter import LengthConversionsReporter

class TestLengthConversionsReporter(unittest.TestCase):

    def test_should_generate_expected_table(self):

        app = LengthConversionsReporter()

        expected_report = '--------------------------------------' + '\n' + \
                          '| Meters | Yards  | Feet   | Inches  |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 100    | 109.36 | 328.08 | 3937.01 |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 101    | 110.45 | 331.36 | 3976.38 |' + '\n' + \
                          '--------------------------------------' + '\n' + \
                          '| 102    | 111.55 | 334.65 | 4015.75 |' + '\n' + \
                          '--------------------------------------'

        self.assertEqual(
            expected_report,
            app.meters_to_english_units('100', '102') 
        )

    def test_should_return_error_message_for_empty_initial_meter(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Cannot process empty amount of meters',
            app.meters_to_english_units('', '102') 
        )

    def test_should_return_error_message_for_empty_final_meter(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Cannot process empty amount of meters',
            app.meters_to_english_units('100', '') 
        )

    def test_should_return_error_message_for_negative_initial_meter(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must be positive',
            app.meters_to_english_units('-100', '102') 
        )

    def test_should_return_error_message_for_negative_final_meter(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must be positive',
            app.meters_to_english_units('100', '-102') 
        )

    def test_should_return_error_message_for_initial_meter_with_value_zero(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must be positive',
            app.meters_to_english_units('0', '102') 
        )

    def test_should_return_error_message_for_final_meter_with_value_zero(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must be positive',
            app.meters_to_english_units('100', '0') 
        )

    def test_should_return_error_message_for_invalid_initial_meters_value(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must contain an integer value',
            app.meters_to_english_units('Not a number', '102') 
        )

    def test_should_return_error_message_for_invalid_final_meters_value(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Amount of meters must contain an integer value',
            app.meters_to_english_units('100', 'Not a number') 
        )

    def test_should_return_error_message_if_initial_meter_is_greater_than_final_meter(self):
        app = LengthConversionsReporter()
        self.assertEqual(
            'Final meter must be greater than initial meter',
            app.meters_to_english_units('102', '100') 
        )