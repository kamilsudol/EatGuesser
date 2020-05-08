from base import Search, log
import os

req = Search(
    recipes_appid=os.environ.get('API_ID'),
    recipes_appkey=os.environ.get('APP_KEY'))

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



