import json

with open("1.json", "r") as f:
    data = json.load(f)

data ["GOLD"] = 1
with open("2.json", "w") as f:
    json.dump(data, f, indent=2)

print(data)
