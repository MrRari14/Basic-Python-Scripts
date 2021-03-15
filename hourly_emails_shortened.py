fn = input("Enter your file name: ")
stored_time = dict()

try:
    opf = open(fn)
except:
    print("Oops, couldn´t find the file/File does not exist.")
    quit()

for line in opf:
    if line.startswith("From "):
        spl = line.split()
        time = spl[5].split(":")
        for hour in spl:
            only_hour = time[0]
        stored_time[only_hour] = stored_time.get(only_hour, 0) + 1
# List comprehension
print(sorted([(v, k) for k, v in stored_time.items()]))
