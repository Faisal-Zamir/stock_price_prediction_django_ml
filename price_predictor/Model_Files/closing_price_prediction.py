import pandas as pd
import numpy as np
import joblib
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained model once
model = joblib.load(os.path.join(BASE_DIR, "stock_prince_prediction_model.pkl"))

def predict_future_prices(start_date, end_date, current_price):
    """
    Predict future stock prices between given dates based on current closing price.
    Returns a list of dictionaries: [{'date': date, 'price': predicted_price}, ...]
    """

    # Prepare future date range
    future_dates = pd.date_range(start=start_date, end=end_date, freq='D')
    df_future = pd.DataFrame({'ds': future_dates})
    df_future['y'] = np.log1p(current_price)  # Apply same transformation

    # Predict
    forecast = model.predict(df_future)
    forecast['predicted_price'] = np.expm1(forecast['yhat'])

    # Format output
    results = [
        {"date": row['ds'].date(), "price": round(row['predicted_price'], 2)}
        for _, row in forecast.iterrows()
    ]
    return results
