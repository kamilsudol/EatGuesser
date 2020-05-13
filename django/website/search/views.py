from django.shortcuts import render
from .models import Recipes
from .api_dir.api_app import Api


def home(request):
	return render(request, 'search/home.html', {'title': 'Home'})

def subsite(request):
	return render(request, 'search/subsite.html', {'title': 'Subsite'})

def results(request):
	query = request.GET.get('q')
	req = Api().ret_req()
	results = req.search_recipe(query)
	context = {
		'database': results # Recipes.objects.all()
	}
	return render(request, 'search/results.html', context)