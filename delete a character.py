infile = "abc.txt"
outfile = "abc2.txt"

a = input('Enter ')
delete_list=list(a)

with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
