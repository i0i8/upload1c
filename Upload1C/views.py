from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def opt(request, date):
    meta = {
        'opt': 'Опт',
        'date': date
    }
    opt_all = SmallOpt.objects.filter(date=date)
    return render(request, 'upload1c/result.html', context={'opt_all': opt_all, 'meta': meta})


def retail(request, date):
    meta = {
        'opt': 'Розница',
        'date': date
    }
    retail = RetailValue.objects.filter(date=date)
    for r in retail:
        print(r.unitate)
    return render(request, 'upload1c/result.html', context={'retail_value': retail, 'meta': meta})


def date(request):
    search_query = request.GET.get('q', '')
    if search_query:
        date = DateLink.objects.filter(date=search_query)
    else:
        date = DateLink.objects.all()
    return render(request, 'upload1c/index.html', context={'date': date})
