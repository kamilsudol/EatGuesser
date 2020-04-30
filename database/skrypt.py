import json

if __name__ == "__main__":
    fields = [
        "name",
        "ingredients",
        "url",
        "image",
        "cookTime",
        "recipeYield",
        "datePublished",
        "prepTime",
        "description"
    ]
    filename = "data"
    dict_main = {}
    dict_temp = {}
    line_read = []

    def format_line(line):
        line = line.replace(f'{fields[index]}', '')
        line = line.replace('"', '')
        line = line.replace('{', '')
        line = line.replace(':', '')
        line = line.replace('\\n', '\n')
        line = line.strip()
        return line

    with open(filename, "r") as data:
        id_no = 1

        for line in data:
            index = 0
            dict_temp = {}
            recipe_id = 'recipe' + str(id_no)
            line_read = list(line.strip().split('",', 9))

            while index < len(fields):
                line_read[index] = format_line(line_read[index])
                dict_temp[fields[index]] = line_read[index]
                index += 1

            dict_main[recipe_id] = dict_temp
            id_no += 1

    database = open("initial_database.json", "w")
    json.dump(dict_main, database, indent = 4)
    database.close()