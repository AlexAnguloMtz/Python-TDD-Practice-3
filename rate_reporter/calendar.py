class Calendar:

    _MONTHS = (
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    )

    @staticmethod
    def is_valid_month(a_month):
        return (a_month) and (any(map(lambda month: month == a_month, Calendar._MONTHS)))

    @staticmethod
    def months_in_a_year():
        return 12