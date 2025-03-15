

import os
import json

FILENAME = "testdict.json"
sample = dict(name="Fred", age = 31, grades = [1, 34, 55])

def write_dict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

directory = os.path.dirname(FILENAME)
if directory and not os.path.exists(directory):
    os.makedirs(directory)

write_dict(sample)