'''
Write a program to read an initial and a final temperature
from the command line. The values will be Fahrenheit degrees.

Print a table showing the equivalences between the Fahrenheit 
degrees and Celsius degrees. 

You should show the results in order, starting with the initial value
and stopping at the final value, adding one Fahrenheit degree for each
row and the Celsius equivalent for each Fahrenheit temperature. 
'''

from temperature_conversion_reporter import TemperatureConversionReporter

def temperatures_table():
    return TemperatureConversionReporter().temperature_conversions(
        input('Enter an initial temperature in Fahrenheit: '),
        input('Enter a final temperature in Fahrenheit: ')
    )

def main():
    print(temperatures_table())

main()