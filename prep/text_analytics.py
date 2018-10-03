import json
from pprint import pprint
from os import listdir
from os.path import isfile, join
from os import walk
import string
import unicodedata, re
import os

def find(name, path):
    for root, dirs, files in walk(path):
        if name in files:
            return os.path.join(root, name)

mypath = "Annotations\\json"
trainpath = "annotations\\prep"
printable = set(string.printable)
for (dirpath, dirnames, filenames) in walk(mypath):
    #print(dirpath, filenames)
    for f1 in filenames:
        #print(f1)
        fname = dirpath + "\\"  + f1
        print(fname)
        with open(fname) as f:
            data =  json.load(f)

            #pprint(data["/document/finalText"])
            #f1.replace('.json', '.txt')
            f1txt = f1[:-5] + ".txt"
            f1txt = trainpath + "\\" + f1txt
            print("After   " + f1txt)
            # Now write this to the pos folder
            #print(find(f1[:-5] + ".txt", trainpath))
            file = open(f1txt ,"wb") 
            filtered_string = ''.join(filter(lambda x:x in string.printable, data["/document/finalText"]))
            #pprint(filtered_string)
            print(len(data["/document/finalText"]))
            print(len(filtered_string))         
            file.write(str(filtered_string).encode('utf8')) 
            file.close()



        
    