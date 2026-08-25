import io
import base64
import qrcode
from django.shortcuts import render
from .models import ShortURL
from .forms import URLShortenerForm
from django.shortcuts import get_object_or_404, redirect

def home_view(request):
    form = URLShortenerForm(request.POST or None)
    new_url = None
    qr_code_base64 = None

    if request.method == 'POST' and form.is_valid():
        original = form.cleaned_data['original_url']
        custom_code = form.cleaned_data.get('custom_code')

        if custom_code:
            # Create explicit entry if custom alias is provided
            obj = ShortURL.objects.create(original_url=original, short_code=custom_code)
        else:
            # Safely fetch the first match to avoid MultipleObjectsReturned
            obj = ShortURL.objects.filter(original_url=original).first()
            if not obj:
                obj = ShortURL.objects.create(original_url=original)

        new_url = request.build_absolute_uri('/') + obj.short_code

        # Generate QR Code
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(new_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        form = URLShortenerForm()  # Reset form

    recent_urls = ShortURL.objects.all().order_by('-created_at')[:5]

    return render(request, 'short/home.html', {
        'form': form,
        'new_url': new_url,
        'qr_code': qr_code_base64,
        'recent_urls': recent_urls
    })

def redirect_view(request, short_code):
    url_obj = get_object_or_404(ShortURL, short_code=short_code)
    url_obj.clicks += 1
    url_obj.save()
    return redirect(url_obj.original_url)