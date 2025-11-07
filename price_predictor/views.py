from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
from .forms import StockPredictForm
from price_predictor.Model_Files.closing_price_prediction import predict_future_prices

def homepage(request):
    predictions = None

    if request.method == "POST":
        form = StockPredictForm(request.POST)
        if form.is_valid():
            current_price = form.cleaned_data['currentPrice']
            start_date = form.cleaned_data['startDate']
            end_date = form.cleaned_data['endDate']

            # Call external prediction function
            predictions = predict_future_prices(start_date, end_date, current_price)
    else:
        form = StockPredictForm()
    print(predictions)
   
    context = {
        "form": form,
        "predictions": predictions,
    }
    return render(request, "price_predictor/homepage.html", context)
