# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

fl_name = input("Please enter your file´s name: ")
try:
    opn_file = open(fl_name)
except:
    print("Either the file doesn´t exist or I did not find it.")
empty_list = list()

for line in opn_file:
    line = line.split()
    for word in line:
        if word in empty_list:
            continue
        else:
            empty_list.append(word)
empty_list.sort()
print(empty_list)
