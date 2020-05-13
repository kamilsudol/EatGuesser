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
	
	helper = req.search_recipe(query)
	checker = {'database': helper}

	flag = False
	for x in checker['database']:
		if x:
			flag = True

	if flag:
		return render(request, 'search/results.html', context)
	else:
		return render(request, 'search/err.html', {'database':{'No matching recipes for: ' + str(query)}})
	