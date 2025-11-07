from django import forms

class StockPredictForm(forms.Form):
    currentPrice = forms.FloatField(
        label="Current Closing Price ($)",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "id": "currentPrice",
                "step": "0.01",
                "placeholder": "e.g., 150.75",
                "required": True,
            }
        )
    )

    startDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "id": "startDate",
                "type": "date",
                "required": True,
            }
        )
    )

    endDate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "id": "endDate",
                "type": "date",
                "required": True,
            }
        )
    )
