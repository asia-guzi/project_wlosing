from django.contrib import admin

# Register your models here.
from .models import Skladnik
admin.site.register(Skladnik)

from .models import Sklad
admin.site.register(Sklad)
