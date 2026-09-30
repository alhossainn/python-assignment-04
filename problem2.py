import json

student = {
    'name': 'Rahim',
    'age': 20,
    'department': 'CSE',
}

data_to_json = json.dumps(student, indent=4)
print(data_to_json)