# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fn = input("Enter file name: ")
stored_emails = dict()

try:
    opfl = open(fn)
except:
    print("Ops, couldn´t read file: ", fn)
    quit()

for line in opfl:
    if line.startswith("From "):
        rline = line.split()
        for email_adress in rline:
            adress = rline[1]
        stored_emails[adress] = stored_emails.get(adress, 0) + 1

bigcount = None
most_prolific_committer = None

for sender, count in stored_emails.items():
    if bigcount is None or count > bigcount:
        most_prolific_committer = adress
        bigcount = count
print(most_prolific_committer, bigcount)
