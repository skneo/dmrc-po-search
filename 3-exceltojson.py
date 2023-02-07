import pandas as pd
import json
import os

dir_path = "files"
def dateFormat(mydate):
    try:
        d,m,y=mydate.split('.')
        return y+'-'+m+'-'+d
    except:
        return mydate
for filename in os.listdir(dir_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(dir_path, filename)
        df = pd.read_excel(file_path)
        result = {}
        for index, row in df.iterrows():
            key = row[4]
            if str(key) == "" or key == "PO Number" or str(key)=="NaN":
                continue
            value = [row[3], dateFormat(str(row[5])), row[7]]
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value]
        json_file = filename.replace(".xlsx", ".json")
        json_file_path = os.path.join(dir_path, json_file)
        with open(json_file_path, "w") as f:
            f.write(json.dumps(result))
 