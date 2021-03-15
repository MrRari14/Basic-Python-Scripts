# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking or bad user data.


print("Hi there, let´s calculate how much you earn per day!")

hours = int(input("How many hours do you work per day?: "))
wage = float(input("I know this is sensitive, but I need to know how much you get paid per hour: "))

print("Your pay: " + str(hours*wage))
