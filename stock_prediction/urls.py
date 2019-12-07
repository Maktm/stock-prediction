"""stock_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import datetime

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

from . import api, models

# def index(request):
#     return HttpResponse("andi oop.")


class stocks:  
    def __init__(stock, symbol, price, change):
        stock.symbol = symbol 
        stock.price = price
        stock.change = change
        
   
# creating list        

def get_current_date() -> str:
    today = datetime.date.today()
    return '{} {} {}, {}'.format(
        today.strftime('%A'),
        today.strftime('%B'),
        today.strftime('%d'),
        today.strftime('%Y')
    )

def dashboard(request):
    return render(request, 'stock_prediction/dashboard.html', {
        'date': get_current_date()
    })

def saved(request):
    saved_stocks = []
    try:
        results = models.SavedStock.objects.filter(user=request.user)
        for r in results:
            saved_stocks.append(stocks('Saved Stock 1', r.name, 'Getting latest price', 'price increase/decrease', 'increase'))
    except Exception as error:
        # Failed to find any saved stocks
        pass

    context= {
        'stocks': saved_stocks,
    }
    return render(request, 'stock_prediction/saved.html', context)

def search(request, keywords=None):
    results = None
    context = {
        'stocks': []
    }
    if not keywords is None:
        results = api.search_stock_quote(keywords)
        stocklist = []
        for r in results:
            stocklist.append(stocks(r.symbol, r.price, r.change))
        context = {
            'stocks': stocklist,
        }

    return render(request, 'stock_prediction/search.html', context)


def details(request, keywords=None):
    
    daily = []
 
    if not keywords is None:
        stockdetail = api.get_stock_quote(keywords)
        stockhistory = api.get_stock_history(keywords)

    for i in range(5):
        daily.append(float(stockhistory[i].price))
       
       
       
           
    context= {
        'stock': stockdetail,
        'daily': daily,
       
        
    }
    return render(request, 'stock_prediction/details.html', context)


def help(request):
    return render(request, 'stock_prediction/help.html')




urlpatterns = [
    path('', dashboard),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('search/<keywords>/', search),
    path('details/<keywords>', details),
    path('accounts/', include('django.contrib.auth.urls')),
    path('help/', help) 
]

