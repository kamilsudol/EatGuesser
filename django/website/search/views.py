from django.shortcuts import render
from .models import Recipes, LikedRecipes
import requests
from .api_dir.api_app import Api
from .labels_dir.label import diet_tags, health_tags
from .except_dir.exceptions import APIError, NotKnownQuery, InvalidKey, \
    InvalidRecipeApiKey, LimitExceeding


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

	if request.method == 'POST':
		if request.POST.get('title') and request.POST.get('description'):
			new_fav = LikedRecipes()
			new_fav.title = request.POST.get('title')
			new_fav.description = request.POST.get('description')
			new_fav.save()

			return render(request,'search/liked_recipes.html')

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
				return render(request, 'search/err.html', {'errorMessage': message})
			else:
				return render(request, 'search/err.html', {'errorMessage': message + "None"})

		if calories_sorting_order:
			context = {
				'database': sorted(req.search_recipe(query), key = lambda recipe: recipe.caloriesPer100), # Recipes.objects.all()
				'dietLabels': dietLabels,
				'healthLabels': healthLabels,
			}
		else:
			context = {
				'database': results, # Recipes.objects.all()
				'dietLabels': dietLabels,
				'healthLabels': healthLabels,
			}
		
		return render(request, 'search/results.html', context)
	
def liked_recipes(request):
	#data = RecipesUpdate(instance=request.user)
	data = LikedRecipes.objects.all()
	context = {
		#'title':data.title,
		#'description':data.description
		'data':data
	}

	return render(request,'search/liked_recipes.html', context)

#def create_fav(request):
	