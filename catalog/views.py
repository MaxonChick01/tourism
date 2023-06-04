from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    popular = Tour.objects.filter(fav=True)
    context = {'cat': 'home', 'popular': popular}
    return render(request, 'index.html', context=context)


def tours(request):
    return redirect('tours_specify', slug='avtobusnyj-tur')


def tours_specify(request, slug):
    def sort_it(sort_params, tours):
        new_params = dict()
        if sort_params['from']:
            tours = tours.filter(price__gte=int(sort_params['from']))
            new_params['from'] = sort_params['from']
        if sort_params['to']:
            tours = tours.filter(price__lte=int(sort_params['to']))
            new_params['to'] = sort_params['to']
        if sort_params['place']:
            tours = tours.filter(place=sort_params['place'])
            new_params['place'] = sort_params['place']
        if sort_params['people']:
            new_params['people'] = sort_params['people']
        if sort_params['date']:
            new_params['date'] = sort_params['date']
        return tours, new_params
    type = Type.objects.get(slug=slug)
    types = Type.objects.all()
    tours = Tour.objects.filter(type_of_tour=type)
    people = ['1', '2', '3', '4', '5']
    places = set([i['place'] for i in Tour.objects.values('place')])
    input_vals = {
        'from': '',
        'to': '',
        'place': 'Не выбрано',
        'people': 'Не выбрано',
        'date': 'Не выбрано'
    }
    if request.method == 'POST':
        tours, input_vals = sort_it(request.POST, tours)
    context = {'types': types,
               'type': type,
               'people': people,
               'tours': tours,
               'places': places,
               'input_vals': input_vals}
    return render(request, 'tours.html', context=context)


def single_tour(request, pk):
    tour = Tour.objects.get(pk=pk)
    tour.description2 = tour.description2.split("\n")
    tour.additional_plces = tour.additional_plces.split("\n") if tour.additional_plces else ""
    context = {'tour': tour}
    return render(request, 'single-tour.html', context=context)
