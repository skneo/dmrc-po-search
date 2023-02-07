import os
import json

dir_in = "withoutNaN"
file_out = "alljson.json"

# initialize an empty dictionary to store all the data
data = {}

# loop through all files in the input directory
for filename in os.listdir(dir_in):
    if filename.endswith(".json"):
        file_in = os.path.join(dir_in, filename)
        with open(file_in, "r") as f:
            file_data = json.load(f)
        # update the data dictionary with the contents of the file_data
        data.update(file_data)

# write the combined data to the output file
with open(file_out, "w") as f:
    json.dump(data, f)
 