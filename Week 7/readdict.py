# readdict.py
# This program reads a dictionary from a file
# author: Loic Bagnoud

import json

FILENAME ="testdict.json"

def readDict():
 with open(FILENAME) as f:
    return json.load(f)


somedict = readDict()

print(somedict)