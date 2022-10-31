import json

f = open('resourcemap.json')

json_dict = json.load(f)

f.close()

key_val = {}

for resource in json_dict["resources"]:
    if resource['latitude']:
        key_val[resource['name']] = resource['id']


with open('language_codes.json', "w") as outfile:
    json.dump(key_val, outfile)








