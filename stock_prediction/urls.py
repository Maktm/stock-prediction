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

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

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
            # get the company info
            saved_stocks.append(stocks(r.symbol, "", 0))
    except Exception as error:
        print(error)

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
            models.SavedStock(user=request.user, symbol=ticker, name='Company').save()
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

def date_to_int(s):
    def to_integer(dt_time):
        return 10000 * dt_time.year + 100 * dt_time.month + dt_time.day
    d = datetime.datetime.strptime(s, "%Y-%m-%d").date()
    return to_integer(d)

def prediction(request, ticker):
    """
    Uses linear regression to generate a prediction for a stock.
    """
    print('[+] generating stock prediction')
    history = api.get_stock_history(ticker)
    dates = []
    prices = []
    for q in history:
        dates.append(date_to_int(q.date))
        prices.append(q.price)
    df = pd.DataFrame(list(zip(dates, prices)), columns=['Date', 'Adj. Close'])
    forecast_out = 30 # number of days to forecast ahead
    df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

    X = np.array(df.drop(['Prediction'], 1))
    X = X[:-forecast_out]

    y = np.array(df['Prediction'])
    y = y[:-forecast_out]

    # 80% training, 20% testing
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    lr = LinearRegression()
    lr.fit(x_train, y_train)

    x_forecast = np.array(df.drop(['Prediction'], 1))[-forecast_out:]
    lr_prediction = lr.predict(x_forecast)

    print(type(lr_prediction))

    return HttpResponse('''{{"predictions": [{}]}}
    '''.format(', '.join([str(e) for e in list(lr_prediction)])))

urlpatterns = [
    path('', dashboard),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('search/<keywords>/', search),
    path('details/<keywords>', details),
    path('accounts/', include('django.contrib.auth.urls')),
    path('prediction/<ticker>/', prediction)
]

