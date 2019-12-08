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
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from . import api, models

class SaveForm(forms.Form):
    ticker = forms.CharField(label='Ticker Symbol')

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
    return render(request, 'stock_prediction/dashboard.html', {'date': get_current_date()})

# def savestock(request):
#     if request.method == 'POST':
#         form = SaveForm(request.POST)

#         if form.is_valid():
#             return HttpResponseRedirect('/saved/')
#     else:
#         form = SaveForm()

#     return render(request, 'search.html', {'form': form})

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
#SAVE FORM
#OBTAINS TICKER NAME UPON CLICKING SAVE
    if request.method == 'POST':
        form = SaveForm(request.POST)

        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            print(ticker)
            return HttpResponseRedirect('/saved/')
    else:
        form = SaveForm()
#END SAVE FORM  

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
            'form': form
        }

    return render(request, 'stock_prediction/search.html', context)


def details(request, keywords=None):
    print('Foo bar {}'.format(keywords))
    daily = []
    stockdetail = None
    stockhistory = None
 
    if not keywords is None:
        try:
            stockdetail = api.get_stock_quote(keywords)
            stockhistory = api.get_stock_history(keywords)

            for i in range(5):
                daily.append(float(stockhistory[i].price))
        except:
            pass

    context= {
        'stock': stockdetail if stockdetail is not None else [],
        'daily': daily if daily is not None else [],
    }
    return render(request, 'stock_prediction/details.html', context)

urlpatterns = [
    path('', dashboard),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('search/<keywords>/', search),
    path('details/<keywords>', details),
    path('accounts/', include('django.contrib.auth.urls')),
   
]

