import re
infile = "database.txt"
outfile = "cleaned_file.txt"

blacklist = ['japanese','bittersweet','skinless','boneless','fresh','cold','warm','hot','baking','all-purpose', 'and', 'freshly', 'ground', 'black', 'red', 'yellow', 'green', 'whole', 'pinch'] 
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in blacklist:
        line = line.replace(word, "")
        line = line.replace("  ", " ")
    fout.write(line)
fin.close()
fout.close()