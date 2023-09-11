from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request, date):
    meta = {
        'opt': 'Опт',
        'retail': 'Розница',
        'date': date
    }
    opt_all = SmallOpt.objects.filter(date=date)
    retail_value = RetailValue.objects.filter(date=date)

    return render(request, 'upload1c/result.html', context={'retail_value': retail_value, 'opt_all': opt_all, 'meta': meta})


def date(request):
    search_query = request.GET.get('q', '')
    if search_query:
        date = DateLink.objects.filter(date=search_query)
    else:
        date = DateLink.objects.all()
    return render(request, 'upload1c/index.html', context={'date': date})
