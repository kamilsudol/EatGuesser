import json
import numpy as np

file = open("data","r")

dict = {
    "recipes": []
}

for x in file:
    #print(str(x))
    dict["recipes"].append(x)

database = open("initial_database.json","w")
database.write(json.dumps(dict))

"""
dict = {
    "recipes":{
        "name": ...
        "ingredients": ...
        etc
        .
        .
    }
}
"""