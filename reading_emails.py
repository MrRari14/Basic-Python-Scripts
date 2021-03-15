# Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.

fn = input('Enter your file name: ')
try:
    op_fn = open(fn)
except:
    print("Could not proceed, could be because: File name is wrong, File was not found, or file type not supported.")
    quit()

count = 0

for line in op_fn:
    if line.startswith('From '):
        count = count + 1
        parsed_line = line.rstrip().split()
        print(parsed_line[1])
    else:
        continue
print('There were', count, 'lines in the file with From as the first word')
