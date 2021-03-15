# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

# Variable declaration.

largest_number = None
smallest_number = None
# Infinite loop that breaks when user inputs 'Done'.
while True:
    inputed_num = input("Please enter numbers. Enter 'Done' when done: ")
    if inputed_num == "Done":
        break
    # Convert variable inputed_nums into integer and store it in new variable: numbers.
    # Catch invalid input and print out a message.
    try:
        number = int(inputed_num)
    except:
        print("Invalid input")
        continue

    # Spit out largest number.
    if largest_number is None and smallest_number is None:
        largest_number = number
        smallest_number = number
    # largest_number = int(inputed_num)
    # smallest_number = int(inputed_num)  
    if number > largest_number:
        largest_number = number

    elif number < smallest_number:
        smallest_number = number

print("Maximum is", largest_number)
print("Minimum is", smallest_number)
