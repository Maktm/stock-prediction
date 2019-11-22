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

from . import api

# def index(request):
#     return HttpResponse("andi oop.")


class stocks:  
    def __init__(stock, name, company, price, change, arrow):
        stock.name = name  
        stock.company = company
        stock.price = price
        stock.change = change
        stock.arrow = arrow
   
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
    stocklist = []  
    stocklist.append( stocks('Saved Stock 1', 'Company', 0, 'price increase', 'increase') ) 
    stocklist.append( stocks('Saved Stock 2', 'Company', 0, 'price increase', 'increase') ) 
    stocklist.append( stocks('Saved Stock 3', 'Company', 0, 'price decrease', 'decrease') )

    context= {
        'stocks': stocklist,
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
            stocklist.append(stocks(r.symbol, '<COMPANY>', r.price, '<DIFFERENCE>', 'increase'))
        context = {
            'stocks': stocklist,
        }

    return render(request, 'stock_prediction/search.html', context)

def details(request):
    stockdetail = stocks('NASDAQ', 'NASDAQ Composite', 7950.86, '+48.67', 'increase') 
    context= {
        'stock': stockdetail,
        }
    return render(request, 'stock_prediction/details.html', context)






# def index(request):
#     return render(request, 'stock_prediction/dashboard.html', {})



urlpatterns = [
    path('', dashboard),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('search/<keywords>/', search),
    path('details/', details),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
