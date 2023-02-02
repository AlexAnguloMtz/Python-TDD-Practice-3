'''
A phone enterprise has decided to 
increment their monthly rate by 4% each month.

Imagine that we are in January 2010 
and the initial rate starts at 57.00 USD.

Write a program to print the monthly
rate for January 2011, 2012, 2013, etc...up to 2035
'''

from rate_reporter import RateReporter

def configured_rates_reporter():
    rate_reporter = RateReporter()
    rate_reporter.currency = 'USD'
    rate_reporter.initial_rate = 57.00
    rate_reporter.monthly_increment_percentage = 4
    return rate_reporter

def rates_table():
    return configured_rates_reporter().calculate_yearly_rates(2010, 2035, 'January')

def main():
    print(rates_table())

main()