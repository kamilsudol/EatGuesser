from ..base_dir.base import Search, log
import os 

class Api:
    def ret_req(self):
        req = Search(
            recipes_appid=os.environ.get('API_ID'),
            recipes_appkey=os.environ.get('APP_KEY')
            )
        return req

    def search(self,query):
        req = self.ret_req()
        for recipe in req.search_recipe(query):
            log.info(f"{recipe}")
            log.info(f"{recipe.calories}")
            log.info(f"{recipe.cautions, recipe.dietLabels, recipe.healthLabels}")
            log.info(f"{recipe.url}")

            for i in recipe.ingredient_quantities:
                log.info(f"{i['text']} ,weight: {i['weight']}")
            log.info("\n")