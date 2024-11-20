from django.shortcuts import render
import qrcode
from .forms import QRCodeForm
from io import BytesIO
from django.core.files.base import ContentFile
from django.http import HttpResponse

def generate_qr_code(request):
    if request.method =='POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
            qr= qrcode.make(text)
            buffer= BytesIO()
            qr.save(buffer,format="PNG")
            buffer.seek(0)
            return HttpResponse(buffer,content_type="image/png")
    else:
        form = QRCodeForm()
    return render(request, 'generate.html', {'form': form})
            
    

