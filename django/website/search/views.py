from django.shortcuts import render
from .models import Recipes
import requests
from .api_dir.api_app import Api
from .labels_dir.label import diet_tags, health_tags


def home(request):
	return render(request, 'search/home.html', {'title': 'Home'})

def subsite(request):
	return render(request, 'search/subsite.html', {'title': 'Subsite'})

def results(request):
	'''
	def flip_order(request):
		calories_sorting_order = request.GET.get('sort')
		if calories_sorting_order is False:
			calories_sorting_order = True
		else:
			calories_sorting_order = False
	'''
	calories_sorting_order = request.GET.get('sort')

	query = request.GET.get('q')

	dietLabels = diet_tags(request)
	healthLabels = health_tags(request)
	
	req = Api().ret_req()
	results = req.search_recipe(query, healthLabels, dietLabels)
	if calories_sorting_order:
		context = {
			'database': sorted(req.search_recipe(query), key = lambda recipe: recipe.calories), # Recipes.objects.all()
			'dietLabels': dietLabels,
			'healthLabels': healthLabels,
		}
	else:
		context = {
			'database': results, # Recipes.objects.all()
			'dietLabels': dietLabels,
			'healthLabels': healthLabels,
		}
	
	helper = req.search_recipe(query, healthLabels, dietLabels)
	checker = {'database': helper}

	flag = False
	for x in checker['database']:
		if x:
			flag = True

	if flag:
		return render(request, 'search/results.html', context)
	else:
		message = 'No matching recipes for: ' + str(query) + ' and filters: '
		for label in healthLabels:
			message += label + ', '

		for label in dietLabels:
			message += label + ', '
		return render(request, 'search/err.html', {'errorMessage': message})
	