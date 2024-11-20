from django import forms

class QRCodeForm(forms.Form):
    text=forms.CharField(label="Enter text for QR code",max_length=300)
    
    