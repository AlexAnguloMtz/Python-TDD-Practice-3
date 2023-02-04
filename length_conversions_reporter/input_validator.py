from utils import StringUtils, Numbers

class InputValidator:

    def validate_input(self, initial_meters, final_meters):
        if (not StringUtils.all_truthy((initial_meters, final_meters))):
            raise ValueError('Cannot process empty amount of meters')

        if (not StringUtils.all_contain_integers((initial_meters, final_meters))):
            raise ValueError('Amount of meters must contain an integer value')

        if (not Numbers.all_positive((int(initial_meters), int(final_meters)))):
            raise ValueError('Amount of meters must be positive')

        if (int(initial_meters) > int(final_meters)):
            raise ValueError('Final measurement must be greater than initial measurement')
