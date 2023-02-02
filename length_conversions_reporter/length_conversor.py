class LengthConversor:

    _METER_TO_YARD_EQUIVALENCE = 1.09361
    _METER_TO_FEET_EQUIVALENCE = 3.28084
    _METER_TO_INCH_EQUIVALENCE = 39.370079

    @staticmethod
    def meters_to_yards(meters):
        return meters * LengthConversor._METER_TO_YARD_EQUIVALENCE

    @staticmethod
    def meters_to_feet(meters):
        return meters * LengthConversor._METER_TO_FEET_EQUIVALENCE

    @staticmethod
    def meters_to_inches(meters):
        return meters * LengthConversor._METER_TO_INCH_EQUIVALENCE
 