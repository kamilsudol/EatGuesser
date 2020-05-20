from django.shortcuts import render
from .models import Recipes
from .api_dir.api_app import Api


def home(request):
	return render(request, 'search/home.html', {'title': 'Home'})

def subsite(request):
	return render(request, 'search/subsite.html', {'title': 'Subsite'})

def results(request):
	query = request.GET.get('q')

	dietLabels = []
	healthLabels = []
	if request.GET.get('blncd'):
		dietLabels.append('balanced')

	if request.GET.get('hprot'):
		dietLabels.append('high-protein')

	if request.GET.get('lfat'):
		dietLabels.append('low-fat')

	if request.GET.get('lcarb'):
		dietLabels.append('low-carb')

	if request.GET.get('vegan'):
		healthLabels.append('vegan')

	if request.GET.get('veg'):
		healthLabels.append('vegetarian')

	if request.GET.get('sugcon'):
		healthLabels.append('sugar-conscious')

	if request.GET.get('pnfree'):
		healthLabels.append('peanut-free')

	if request.GET.get('tnfree'):
		healthLabels.append('tree-nut-free')

	if request.GET.get('alcfree'):
		healthLabels.append('alcohol-free')

	req = Api().ret_req()
	results = req.search_recipe(query, healthLabels, dietLabels)
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
	