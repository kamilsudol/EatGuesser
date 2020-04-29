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
line_read = []

with open(filename, "r") as data:
    index = 0
    id_no = 1

    for line in data:
        index = 0
        dict_temp = {}
        line_read = list(line.strip().split('",', 9))


        recipe_id = 'recipe' + str(id_no)

        # print(line_read)
        while index < len(fields):
            line_read[index] = line_read[index].replace(f'{fields[index]}', '')
            line_read[index] = line_read[index].replace('"', '')
            line_read[index] = line_read[index].replace('{', '')
            line_read[index] = line_read[index].replace(':', '')
            line_read[index] = line_read[index].replace('\\n', '\n')
            line_read[index] = line_read[index].strip()
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
