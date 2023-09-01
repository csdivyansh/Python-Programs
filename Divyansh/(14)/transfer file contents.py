sFile = input(("Enter the Name of Source File: "))
tFile = input(("Enter the Name of Target File: "))

fp= open(sFile, "r")
texts = fp.readlines()
fp.close()

fp = open(tFile, "a")
for s in texts:
    fp.write(s)
fp.close()

print("File Copied Successfully!")
