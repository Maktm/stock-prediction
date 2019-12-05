from django.shortcuts import render

def dashboard(request):
    return render(request, 'stock_prediction/dashboard.html', {})