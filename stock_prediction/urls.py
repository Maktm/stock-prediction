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
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

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



def dashboard(request):
    return render(request, 'stock_prediction/dashboard.html', {})

def saved(request):
    stocklist = []  
    stocklist.append( stocks('Saved Stock 1', 'Company', 0, 'price increase', 'increase') ) 
    stocklist.append( stocks('Saved Stock 2', 'Company', 0, 'price increase', 'increase') ) 
    stocklist.append( stocks('Saved Stock 3', 'Company', 0, 'price decrease', 'decrease') )

    context= {
        'stocks': stocklist,
        }
    return render(request, 'stock_prediction/saved.html', context)

def search(request):
    stocklist = []  
    stocklist.append( stocks('NASDAQ', 'NASDAQ Composite', 7950.86, '+48.67', 'increase') ) 
    stocklist.append( stocks('AAPL', 'Apple Inc.', 230.09, '1.040T', 'increase') ) 
    stocklist.append( stocks('SBUX', 'Starbucks Corporation', 85.82, '102.7B', 'decrease') )

    context= {
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
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('details/', details),
]
