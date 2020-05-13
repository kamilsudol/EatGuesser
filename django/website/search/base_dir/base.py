import requests
import json
import logging as log
from ..except_dir.exceptions import APIError, NotKnownQuery, InvalidKey, \
    InvalidRecipeApiKey
import numpy as np

log.basicConfig(filename='output.log', level=log.INFO,
                format='%(message)s')


class API(object):

    def __init__(self, recipes_appid=None, recipes_appkey=None):
        self.recipes_appid = recipes_appid
        self.recipes_appkey = recipes_appkey

    def search_recipe(self, query="pizza"):
        url = 'https://api.edamam.com/search?q=' + query + '&app_id=' + \
              self.recipes_appid + '&app_key=' + \
              self.recipes_appkey

        r = requests.get(url)
        if r.status_code == 401:
            raise InvalidRecipeApiKey
        return r.json()


class Search(API):

    def search_recipe(self, query="pizza"):
        data = super().search_recipe(query)
        hits = data["hits"]
        for hit in hits:
            data = hit["recipe"]
            data["yields"] = data["yield"]
            data.pop("yield")
            data["ingredient_names"] = data["ingredientLines"]
            data.pop("ingredientLines")
            data["share_url"] = data["shareAs"]
            data.pop("shareAs")
            yield Recipe(edamam=self, **data)


class Recipe:
    def __init__(self,
                 label,
                 uri="",
                 url="",
                 share_url="",
                 image=None,
                 dietLabels=None,
                 healthLabels=None,
                 yields=1.0,
                 cautions=None,
                 totalDaily=None,
                 totalWeight=0,
                 calories=0,
                 totalTime=0,
                 totalNutrients=None,
                 digest=None,
                 ingredients=None,
                 source="edamam",
                 ingredient_names=None,
                 edamam=None):
        self.ingredient_names = ingredient_names or []
        self.ingredient_quantities = ingredients or []
        self.label = label
        self.dietLabels = dietLabels or []
        self.healthLabels = healthLabels or []
        self.uri = uri
        self.url = url or self.uri
        self.share_url = share_url or self.url
        self.yields = yields
        self.cautions = cautions
        self.totalDaily = []
        self.totalDaily = totalDaily or []
        self.totalWeight = np.round(totalWeight,2)
        self.calories = np.round(calories,2)
        self.totalTime = totalTime
        self.totalNutrients = []
        self.totalNutrients = totalNutrients or []
        self.image = image
        if isinstance(digest, list):
            self.digest = {}
            for content in digest:
                self.digest[content["label"]] = content
        else:
            self.digest = digest or {}
        self.__edamam = edamam or API()

    def __str__(self):
        return self.label
