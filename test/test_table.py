import unittest
from table import Table, InvalidRowException

class TestTable(unittest.TestCase):

    def test_should_return_correct_string_representation(self):

        table = Table(('Animals', 'Colors'))
        table.add_rows((
            ('Bird', 'Green'),
            ('Frog', 'Blue')
        ))

        expected_table = '--------------------' + '\n' + \
                         '| Animals | Colors |' + '\n' + \
                         '--------------------' + '\n' + \
                         '| Bird    | Green  |' + '\n' + \
                         '--------------------' + '\n' + \
                         '| Frog    | Blue   |' + '\n' + \
                         '--------------------'   
        
        self.assertEqual(expected_table, str(table))

    def test_keeps_track_of_number_of_columns(self):
        table = Table(('Animals', 'Colors'))
        self.assertEqual(2, table.columns)

    def test_keeps_track_of_number_of_rows(self):
        table = Table(('Animals', 'Colors'))
        table.add_rows((
            ('Dog', 'Brown'), 
            ('Bird', 'Green'),
            ('Butterfly', 'Blue')
        ))
        
        self.assertEqual(3, table.rows)

    def test_raises_invalid_row_exception_when_adding_row_longer_than_number_of_columns(self):
        table = Table(tuple('Animals'))
        self.assertRaises(
            InvalidRowException, 
            lambda: table.add_row('Dog', 'Brown')
        )

    def test_raises_exception_when_adding_a_row_that_is_shorter_than_number_of_columns(self):
        table = Table(('Animals', 'Colors'))
        self.assertRaises(
            InvalidRowException, 
            lambda: table.add_row('Dog')
        )

    def test_raises_exception_when_constructor_argument_is_not_a_tuple(self):
        self.assertRaises(
            TypeError, 
            lambda: Table(['Animals', 'Colors'])
        )