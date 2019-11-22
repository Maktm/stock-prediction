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
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("andi oop.")

def dashboard(request):
    return render(request, 'stock_prediction/dashboard.html', {})

def saved(request):
    return render(request, 'stock_prediction/saved.html', {})

def search(request):
    return render(request, 'stock_prediction/search.html', {})

def details(request):
    return render(request, 'stock_prediction/details.html', {})




# def index(request):
#     return render(request, 'stock_prediction/dashboard.html', {})



urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('saved/', saved),
    path('search/', search),
    path('details/', details),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
