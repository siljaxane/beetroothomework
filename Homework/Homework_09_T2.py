import json 
import pprint

Phonebook = ()

first_person = {
    'first_name': 'Ian',
    'second_name': 'Sims', 
    'full_name': 'Ian Sims'
    'telephone_number': '12345',
    'city': 'Brighton'
}

phonebook = [first_person]
json.dumps(Phonebook)

json_string = json.dumps(Phonebook)
print(json_string)

with open('data.json', 'w') as f:
    f.write(json_string)

append_dict = {'first_name': 'Lisa'}
x = json.loads(first_person)
x.update(append_dict)
print(json.dumps(x))

json_string.close()

print('original data:')
pprint.pprint(Phonebook)

