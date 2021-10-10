import json

with open("example.json") as f:
    data = json.load(f)


# print(data)
print(data['glossary']['GlossDiv'])


new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open("new_json.json", 'w') as f:
    json.dump(new_json, f)

with open("new_json.json", 'r') as f:
    new_json_reload = json.load(f)

print(new_json_reload)
print(type(new_json_reload['key2']))
print(new_json_reload['key2'])

json_str = json.dumps(new_json)
print(type(json_str))

python_data = json.loads(json_str)
print(python_data)
print(type(python_data))