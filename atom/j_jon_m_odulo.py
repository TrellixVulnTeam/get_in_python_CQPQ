import json

people_string = '''
{
    "people": [
    {
        "name": "John Smith",
        "phone": "615-555-7164",
        "emails": ["john@gmail.com", "john.smith@gmail.com"],
        "has_license": false
    },
    {
        "name": "Jone Doe",
        "phone": "777-555-7164",
        "emails": null,
        "has_license": true
    }
  ]
}
'''

data = json.loads(people_string)

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
