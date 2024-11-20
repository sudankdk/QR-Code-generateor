from django.shortcuts import render
import qrcode
from .forms import QRCodeForm
from io import BytesIO
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            text = form.cleaned_data['text']
            image = form.cleaned_data.get('image')  # Get uploaded image

            # Check if an image was uploaded
            if image:
                # Save the image to the media folder
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                image_url = fs.url(filename)  # URL of the uploaded image

                # Generate QR code containing the image URL
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(image_url)  # Add the URL of the uploaded image to the QR code
                qr.make(fit=True)

                # Create the image of the QR code
                qr_img = qr.make_image(fill='black', back_color='white')

                # Return the QR code image as a response
                response = HttpResponse(content_type='image/png')
                qr_img.save(response, 'PNG')
                return response

            else:
                # If no image is uploaded, you can generate QR for text (default behavior)
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
                qr.add_data(text)
                qr.make(fit=True)

                qr_img = qr.make_image(fill='black', back_color='white')
                response = HttpResponse(content_type='image/png')
                qr_img.save(response, 'PNG')
                return response

    else:
        form = QRCodeForm()

    return render(request, 'generate.html', {'form': form})
