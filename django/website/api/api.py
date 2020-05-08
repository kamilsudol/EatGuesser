from base import Search, log
<<<<<<< HEAD
import os
=======
>>>>>>> 4e386617ee3352426ea0cbe89ab6694800dd7d8a

req = Search(
    recipes_appid='0b1a1954',
    recipes_appkey='e3dc699ff1678979bc89ed33f6d01f8d')

question = "Type the ingredient you want for recipe to include:\n"
query = input(question)
log.info(f"{question}You have chosen: {query}")


for recipe in req.search_recipe(query):
    log.info(f"{recipe}")
    log.info(f"{recipe.calories}")
    log.info(f"{recipe.cautions, recipe.dietLabels, recipe.healthLabels}")
    log.info(f"{recipe.url}")

    for i in recipe.ingredient_quantities:
        log.info(f"{i['text']} ,weight: {i['weight']}")
    log.info("\n")



