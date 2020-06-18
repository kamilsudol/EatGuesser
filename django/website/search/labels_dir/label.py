def diet_tags(request):
    dietLabels = []

    if request.GET.get('blncd'):
        dietLabels.append('balanced')

    if request.GET.get('hprot'):
        dietLabels.append('high-protein')

    if request.GET.get('lfat'):
        dietLabels.append('low-fat')

    if request.GET.get('lcarb'):
        dietLabels.append('low-carb')

    return dietLabels

def health_tags(request):
    healthLabels = []

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

    return healthLabels