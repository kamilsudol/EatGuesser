from django.shortcuts import render
from .models import Recipes, LikedRecipes, ShoppingList
import requests
import json
import os
from .api_dir.api_app import Api
from .labels_dir.label import diet_tags, health_tags
from .except_dir.exceptions import APIError, NotKnownQuery, InvalidKey, \
    InvalidRecipeApiKey, LimitExceeding


def home(request):
	ret_shopp = subsite2(request)
	if(ret_shopp):
		return ret_shopp
	file = open("staticfiles/hint_products.json", "r").read()
	data = json.loads(file)
	return render(request, 'search/home.html', {'title': 'Home', 'jsonData': data})



def subsite2(request):
	file = open("staticfiles/hint_products.json", "r").read()
	data = json.loads(file)
	if request.method == 'POST':
		if request.POST.get('ingredients'):
			new_ing = ShoppingList()
			new_ing.ingredients = request.POST.get('ingredients')
			new_ing.save()

			return render(request, 'search/err.html', {'errorMessage': 'Shopping list has been updated successfully!', 'jsonData': data})

def results(request):
	file = open("staticfiles/hint_products.json", "r").read()
	data = json.loads(file)

	ret_shopp = subsite2(request)
	if(ret_shopp):
		return ret_shopp

	if request.method == 'POST':
		if request.POST.get('title') and request.POST.get('description'):
			new_fav = LikedRecipes()
			new_fav.title = request.POST.get('title')
			new_fav.description = request.POST.get('description')
			new_fav.save()

			return render(request, 'search/err.html', {'errorMessage': 'Recipe has been added successfully!', 'jsonData': data})

	else:
		
		calories_sorting_order = request.GET.get('sort')

		query = request.GET.get('q')

		dietLabels = diet_tags(request)
		healthLabels = health_tags(request)
		
		req = Api().ret_req()
		results = req.search_recipe(query, healthLabels, dietLabels)
		if next(results) == -1:
			return render(request, 'search/err.html', {'errorMessage': 'You have exceeded api limit, wait a few seconds.'})
		elif next(results) == -2:
			message = 'No matching recipes for: ' + str(query) + ' and filters: '
			
			flag2 = []
			for label in healthLabels:
				flag2.append(label)
				message += label + ', '

			for label in dietLabels:
				flag2.append(label)
				message += label + ', '
			print("brak wyników wyszukiwania")
			if not flag2:
				return render(request, 'search/err.html', {'errorMessage': message, 'jsonData': data})
			else:
				return render(request, 'search/err.html', {'errorMessage': message + "None", 'jsonData': data})

		if calories_sorting_order:
			context = {
				'database': sorted(req.search_recipe(query), key = lambda recipe: recipe.caloriesPer100),
				'dietLabels': dietLabels,
				'healthLabels': healthLabels,
				'jsonData': data
			}
		else:
			context = {
				'database': results,
				'dietLabels': dietLabels,
				'healthLabels': healthLabels,
				'jsonData': data
			}
		
		return render(request, 'search/results.html', context)
	
def liked_recipes(request):
	ret_shopp = subsite2(request)
	if(ret_shopp):
		return ret_shopp
	data = LikedRecipes.objects.all()
	context = {

		'data':data
	}

	return render(request,'search/liked_recipes.html', context)

def subsite(request):
	ret_shopp = subsite2(request)
	if(ret_shopp):
		return ret_shopp
	map_box = os.environ.get('MAP_KEY')
	data = ShoppingList.objects.last()
	location = requests.get('https://ipinfo.io/')
	location_data = location.json()
	loc = location_data['loc']

	context = {
		'data':data,
		'token':map_box,
		'loc_data': loc
	}

	return render(request,'search/subsite.html', context)
	