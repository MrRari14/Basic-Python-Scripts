print("Hello, welcome to Bernardo´s simple calculator!")

num1 = float(input("Please enter your first number: "))
op = input("Now enter the desired operation (+,-.,*,/): ")
num2 = float(input("Lastly, enter your second number: "))

if op == "+":
    print("The result is: " + str(num1 + num2))
elif op == "-":
    print("The result is: " + str(num1 - num2))
elif op == "*":
    print("The result is: " + str(num1 * num2))
elif op == "/":
    print("The result is: " + str(num1 / num2))
else:
    print("The operation is invalid :(...")
