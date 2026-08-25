import string
import random
from django.db import models

def generate_short_code():
    length = 6
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=length))
        if not ShortURL.objects.filter(short_code=code).exists():
            return code

class ShortURL(models.Model):
    original_url = models.URLField(max_length=500)
    # Allow blank in form, but default to random generator if left empty
    short_code = models.CharField(max_length=20, unique=True, blank=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"