import re
from django import forms
from .models import ShortURL

class URLShortenerForm(forms.ModelForm):
    custom_code = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm',
            'placeholder': 'Custom alias (optional, e.g., my-link)',
        })
    )

    class Meta:
        model = ShortURL
        fields = ['original_url']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm',
                'placeholder': 'Enter long URL here (https://example.com)',
            })
        }

    def clean_custom_code(self):
        custom_code = self.cleaned_data.get('custom_code', '').strip()
        if not custom_code:
            return custom_code

        # Only allow alphanumeric characters, hyphens, and underscores
        if not re.match(r'^[a-zA-Z0-9_-]+$', custom_code):
            raise forms.ValidationError("Custom alias can only contain letters, numbers, hyphens, and underscores.")

        # Reserve special system routes
        if custom_code.lower() in ['admin', 'login', 'logout', 'api']:
            raise forms.ValidationError("This alias is reserved by the system.")

        # Check for existing code in database
        if ShortURL.objects.filter(short_code=custom_code).exists():
            raise forms.ValidationError("This custom alias is already taken. Try another.")

        return custom_code