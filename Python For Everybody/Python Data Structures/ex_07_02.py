# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        index = line.find(' ')
        number = float(line[index+1:])
        total = total+ number
        count +=1


ans = total/count
print("Average spam confidence: "+ str(ans))
