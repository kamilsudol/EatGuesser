import json
# import numpy as np

fields = ["name",
          "ingredients",
          "url",
          "image",
          "cookTime",
          "recipeYield",
          "datePublished",
          "prepTime",
          "description"]

filename = "data"
dict_main = {}
dict_temp = {}

with open(filename, "r") as data:
    index = 0
    id_no = 1

    for line in data:
        line_read = list(line.strip().split('",', 9))

        # print(line_read)

        recipe_id = 'recipe' + str(id_no)

        while index < len(fields):
            dict_temp[fields[index]] = line_read[index]
            index += 1

        dict_main[recipe_id] = dict_temp
        id_no += 1

database = open("initial_database.json", "w")
json.dump(dict_main, database, indent = 4)
database.close()


# for x in file:
#     #print(str(x))
#     dict["recipes"].append(x)

# database = open("initial_database.json","w")
# database.write(json.dumps(dict))


# dict = {
#     "recipes":{
#         "name": ...
#         "ingredients": ...
#         etc
#         .
#         .
#     }
# }
