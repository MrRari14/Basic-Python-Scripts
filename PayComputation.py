# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.
# The function should return a value. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
# Do not name your variable sum or use the sum() function.

hours = input("Hi there, please tell me how many hours you´ve worked: ")
hours = float(hours)
rate_per_hour = input("Now, please tell me your rate per hour: ")
rate_per_hour = float(rate_per_hour)


def computepay():
    if hours <= 40:
        gross_pay = hours * rate_per_hour
        return gross_pay
    elif hours > 40:
        normal_pay = 40 * rate_per_hour
        extra_hours_pay = (hours - 40) * (rate_per_hour * 1.5)
        gross_pay = normal_pay + extra_hours_pay
        return gross_pay


print("Pay", computepay())
