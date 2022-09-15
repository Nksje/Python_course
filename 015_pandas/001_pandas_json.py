import pandas as pd
import json

# Open file and load it with JSON module first
with open('json_files//sample2.json', 'r', encoding='UTF8') as file:
    data = json.load(file)

# pd.DataFrame is used to convert json data into data frame
df = pd.DataFrame(data['people'])

print(df)
print(type(df))
