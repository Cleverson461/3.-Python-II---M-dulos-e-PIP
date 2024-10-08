import json 

# 1 - Strings para Dicionários
person = '{"name": "Cleverson", "languagens":["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['languagens'])
print()

# 2 - Convertando dicionário para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))
print()

# 3 - Formantando Json
print(json.dumps(person_dict, indent=4, sort_keys=True))
print()

# 4 - Salvado json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)
    
print()
# 5 - Lendo json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)