# forms.py
from django import forms

class QRCodeForm(forms.Form):
    text = forms.CharField(max_length=500, required=True)
    image = forms.ImageField(required=False)  # Optional image field
