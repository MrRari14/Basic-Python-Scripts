# Write a program that prompts for a file name.
# Then opens that file and reads through the file.
# And print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

fname = input("Please type your file name: ")
try:
    fl = open(fname)
except:
    print("Sorry, either I cannot find the file or it doesn´t exist.")

for lines in fl:
    print(lines.upper().strip())
