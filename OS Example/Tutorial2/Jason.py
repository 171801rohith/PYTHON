import json

privelege = '''{"PREMIUM": 100000,"GOLD": 50000,"SILVER": 25000 }'''
data = json.loads(privelege)
print(data["PREMIUM"])
data["BRONZE"] = 100
new_json = json.dumps(data, indent=2)
print(new_json)