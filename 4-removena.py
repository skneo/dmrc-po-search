import os
import json

def remove_NaN(file):
    with open(file, "r") as f:
        data = json.load(f)
    data = {k: v for k, v in data.items() if k != "NaN"}
    return data

dir_in = "allpo"
dir_out = "withoutNaN"

# create the output directory if it doesn't exist
if not os.path.exists(dir_out):
    os.makedirs(dir_out)

# loop through all files in the input directory
for filename in os.listdir(dir_in):
    if filename.endswith(".json"):
        file_in = os.path.join(dir_in, filename)
        data = remove_NaN(file_in)
        file_out = os.path.join(dir_out, filename)
        with open(file_out, "w") as f:
            json.dump(data, f)
 