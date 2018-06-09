from django.shortcuts import render, get_object_or_404, redirect
from .models import Mineral
from .forms import SearchForm
from random import randint

# Create your views here.


def all_minerals(request):
    mineral_list = Mineral.objects.all()
    return render(request, 'minerals/minerals.html',
                  {'mineral_list': mineral_list})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_random(request):
    random_pk = randint(1, Mineral.objects.count())
    mineral = get_object_or_404(Mineral, pk=random_pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_filter(request, string):
    mineral_list = Mineral.objects.filter(name__startswith=string)
    return render(request, 'minerals/minerals.html',
                  {'mineral_list': mineral_list,
                   'current_filter': string})


def mineral_group(request, group_name):
    mineral_list = Mineral.objects.filter(group=group_name)
    return render(request, 'minerals/minerals.html',
                  {'mineral_list': mineral_list,
                   'current_group_filter': group_name})


def mineral_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            mineral_list = Mineral.objects.filter(name__iregex=search_text)
            return render(request, 'minerals/minerals.html',
                          {'mineral_list': mineral_list})
    else:
        return redirect('minerals:list')
