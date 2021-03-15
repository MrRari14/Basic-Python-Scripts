# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Average spam confidence: 0.7507185185185187


file_name = input("Please enter your file name: ")
count = 0
tot = 0.0

try:
    open_file = open(file_name)
except: 
    print("Sorry, either I cannot find the file or it doesn´t exist.")
for line in open_file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        chop = line[19:]
        numbers = float(chop)
        tot = tot + numbers
        average = (tot/count)
      
print("Average spam confidence:", average)
