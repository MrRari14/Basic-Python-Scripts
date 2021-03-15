flnm = input("Enter file name: ")
storage = dict()

try:
    opfl = open(flnm)
except: 
    print("Can´t open that file:", flnm)
    quit()

for line in opfl:
    words = line.split()
    for word in words:
        if word not in storage:
            storage[word] = 1
        else:
            storage[word] = storage[word] + 1
print(storage)
