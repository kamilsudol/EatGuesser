from django.shortcuts import render
from .models import Recipes
from .api_dir.api_app import Api

req = Api().ret_req()
database2 = req.search_recipe("chicken") # tutaj musimy jakos przekazac stringa uzytkownika
										 # albo zmienic strukture tego co mamy jakos, i dunno


def home(request):
	context = {
		'database': database2 # Recipes.objects.all()
	}
	return render(request, 'search/home.html', context)

def subsite(request):
	return render(request, 'search/subsite.html', {'title': 'Subsite'})
