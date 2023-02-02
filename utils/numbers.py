class Numbers:

    @staticmethod
    def is_valid_float(input):
        try:
            float(input)
            return True
        except Exception:
            return False

    @staticmethod
    def all_positive(numbers):
        return all(map(lambda number: number > 0, numbers))