import json

with open("data.json", "r") as f:
    data = json.load(f)

data ["GOLD"] = 1909
with open("data1.json", "w") as f:
    json.dump(data, f, indent=2)

print(data)
