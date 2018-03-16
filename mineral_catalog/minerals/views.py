from django.shortcuts import render, get_object_or_404
from .models import Mineral
from random import randint

# Create your views here.


def mineral_list(request):
    all_minerals = Mineral.objects.all()
    return render(request, 'minerals/minerals.html',
                  {'all_minerals': all_minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_random(request):
    random_pk = randint(1, Mineral.objects.count())
    mineral = get_object_or_404(Mineral, pk=random_pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})
