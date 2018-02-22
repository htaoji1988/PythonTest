import json


data = {1: None}

json_str = json.dumps(data)
print(data)
print(json_str)

with open("json_test.json", "w") as f:
    json.dump(data, f)
