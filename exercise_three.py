'''
Write a program that can read from the command line 
an initial and final measurement in meters, and convert those
meters to yards, feet and inches.

You must print a table with all the equivalences, 
starting at the initial measurement, adding one meter
for each row, and stopping at the final measurement.

In each row you should print the equivalences between 
meters and all the units mentioned before.
'''
from length_conversions_reporter import LengthConversionsReporter

def conversions_table():
    return LengthConversionsReporter().meters_to_english_units(
        input('Enter your initial measurement in meters: '),
        input('Enter your final measurement in meters: ')
    ) 

def main():
    print(conversions_table())

main()