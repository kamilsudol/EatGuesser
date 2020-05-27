import requests
import json
import logging as log
from ..except_dir.exceptions import APIError, NotKnownQuery, InvalidKey, \
    InvalidRecipeApiKey, LimitExceeding
import numpy as np

log.basicConfig(filename='output.log', level=log.INFO,
                format='%(message)s')


class API(object):

    def __init__(self, recipes_appid=None, recipes_appkey=None):
        self.recipes_appid = recipes_appid
        self.recipes_appkey = recipes_appkey

    def search_recipe(self, query="pizza", healthLabels = [], dietLabels = []):
        health = ""
        for label in healthLabels:
            health = health + "&health=" + label

        diet = ""
        for label in dietLabels:
            diet = diet + "&diet=" + label
        url = 'https://api.edamam.com/search?q=' + query + '&app_id=' + \
              self.recipes_appid + '&app_key=' + \
              self.recipes_appkey + health + diet
        r = requests.get(url)
        if r.status_code == 401:
            raise InvalidRecipeApiKey
        elif r.status_code == 429:
            raise LimitExceeding
        return r.json()


class Search(API):

    def search_recipe(self, query="pizza", healthLabels = [], dietLabels = []):
        try:
            data = super().search_recipe(query, healthLabels, dietLabels)
        except LimitExceeding:
            yield -1
            yield -1
        hits = data["hits"]
        if data["count"] == 0:
            print("test1")
            yield -2
            yield -2
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
        for x in ingredients:
            x['weight'] = np.round(x['weight'],2)
        self.ingredient_quantities = ingredients
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
        self.totalWeight = totalWeight
        self.calories = int(calories)
        self.caloriesPer100 = int(calories*100/totalWeight)
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
