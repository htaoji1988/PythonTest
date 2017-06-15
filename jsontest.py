import json

config_data = open("666")
config = json.load(config_data)
config_data.close()
print(config["firstName"])