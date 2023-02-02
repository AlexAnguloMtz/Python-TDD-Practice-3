class Table:

    def __init__(self, columns):
        if(not isinstance(columns, tuple)):
            raise TypeError('Columns must be a Tuple')

        self._table = []
        for column in columns:
            self._table.append([column])

    def add_row(self, *row):
        self._assert_is_valid_row(row)
        row_strings = list(map(str, row))
        for column_index in range(self.columns):
            self._column(column_index).append(row_strings[column_index])

    def add_rows(self, rows):
        for row in rows:
            self.add_row(*row)

    @property
    def columns(self):
        return len(self._table)

    @property
    def rows(self):
        rows_without_headers = self.rows_with_headers - 1
        return rows_without_headers
    
    @property
    def rows_with_headers(self):
        return len(self._column(0))

    def _column(self, column_index):
        return self._table[column_index]

    def _row(self, row_index):
        row = []
        for column in range(self.columns):
            row.append(self._column(column)[row_index])
        return row

    def _assert_is_valid_row(self, row):
        if (len(row) != self.columns):
            raise InvalidRowException()

    def _longest_word_in_column(self, column_index):
        longest_word_in_column = ''
        for row_index in range(self.rows_with_headers):
            if (len(self._word_at(column_index, row_index)) > len(longest_word_in_column)):
                longest_word_in_column = self._word_at(column_index, row_index)
        return longest_word_in_column

    def _word_at(self, column_index, row_index):
        return self._column(column_index)[row_index]

    def _format_row(self, row_index):
        
        row = self._row(row_index)

        formatted_row = f'{self._horizontal_separator()}\n'

        for word_index in range(len(row)):
            current_word = row[word_index]
            difference_between_longest_word_and_current_word = \
                (len(self._longest_word_in_column(word_index)) - len(current_word))

            formatted_row += self._vertical_separation_char()
            formatted_row += self._space_char(1)
            formatted_row += current_word
            formatted_row += self._space_char(difference_between_longest_word_and_current_word)
            formatted_row += self._space_char(1)

        return f'{formatted_row}{self._vertical_separation_char()}\n'

    def _horizontal_separator(self):
        horizontal_separator = ''
        for word in self._longest_word_in_each_column():
            horizontal_separator += (self._horizontal_separation_char(len(word)))

        horizontal_separator += (self._horizontal_separation_char(self._amount_of_extra_white_spaces()))
        horizontal_separator += (self._horizontal_separation_char(self._amount_of_vertical_separators()))
        
        return horizontal_separator

    def _longest_word_in_each_column(self):
        longest_word_in_each_column = []
        for column in range(self.columns):
            longest_word_in_each_column.append(self._longest_word_in_column(column))
        return longest_word_in_each_column

    def _horizontal_separation_char(self, amount):
        return '-' * amount

    def _vertical_separation_char(self):
        return '|'

    def _space_char(self, amount):
        return ' ' * amount

    def _amount_of_vertical_separators(self):
        return self.columns + 1

    def _amount_of_extra_white_spaces(self):
        return self.columns * 2 

    def __str__(self):
        formatted_table = ''
        for row in range(self.rows_with_headers):
            formatted_table += self._format_row(row)
        return f'{formatted_table}{self._horizontal_separator()}'


class InvalidRowException(Exception):
    pass