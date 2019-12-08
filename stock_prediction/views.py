"""
    views.py

    This module contains all of the views that resolve to HttpResponse
    objects sent back to the client. They are the processing points
    of the entire Django application and turn input into output.
"""

from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    """
    Generates the homepage for a user dynamically and
    returns it in an HttpResponse.
    """
    return render(request, 'index.html', {
        'date': datetime.now().strftime('%A, %B %d %Y')
    })

def search(request: HttpRequest, keywords: str = None) -> HttpResponse:
    """
    Either returns the search page as an HttpResponse
    or searches for a term, when specified, then
    provides the results inside of the HTML code.
    """
    context = dict()
    if keywords is not None:
        pass
    return render(request, 'search.html', context)

def saved(request: HttpRequest) -> HttpResponse:
    """
    Returns the HTML code that describes all the stocks
    that have been saved for the current user.
    """
    return render(request, 'saved.html')

def detail(request: HttpRequest) -> HttpResponse:
    """
    Returns a page that describes information about a
    single stock in an HttpResponse object.
    """
    return render(request, 'detail.html')

def help_page(request: HttpRequest) -> HttpResponse:
    """
    Returns the help page. The help page displays information
    about the app, how to use it etc.
    """
    return render(request, 'help.html')