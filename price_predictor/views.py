from django.shortcuts import render

def homepage(request): 
    return render(request, 'price_predictor/homepage.html')