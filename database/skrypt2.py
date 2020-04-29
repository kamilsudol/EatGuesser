import json

file = open("initial_database.json","r")
data = json.loads(file.read())

print(data)

for x in data["recipes"]:
    #print(x)
    #print(x["name"])
    pass