import os
filename = input("File to format: ")
os.system("gunzip "+filename)
n = int(input("What number genome is this? "))
os.system("mv "+filename[:-3]+" genome"+str(n)+".fna")
original = "genome"+str(n)+".fna"
copy = "genome"+str(n)+"_copy.fna"
filtered = "genome"+str(n)+"_filtered.fna"
rem = ['>']
with open(original) as old, open(copy,'w') as new:
    for line in old:
        if not any(bad in line for bad in rem):
            new.write(line)
with open(copy) as f, open(filtered,'a') as f2:
    f2.write("".join(line.strip() for line in f))
with open(filtered, 'r+') as inp:
    y = inp.read().upper()
    inp.truncate(0)
with open(filtered, 'a') as out:
    out.write(y)
os.remove(copy)
