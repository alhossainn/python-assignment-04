import json

student = {
    'name': 'Rahim',
    'age': 20,
    'department': 'CSE',
}

data_to_json = json.dumps(student)
print(data_to_json)