import pandas as pd
import json, os

df = pd.read_csv("fake_timesheets.csv")
content = []

for index, row in df.iterrows():
    content.append(row.to_dict())

print(content)

with open("jsonfile.json", 'w') as f:
    json.dump(content, f, indent=4)


print(os.path.getsize("jsonfile.json") / 1024**2)