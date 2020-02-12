import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "*.png"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
