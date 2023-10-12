from django.contrib import admin

# Register your models here.
from .models import Składnik
admin.site.register(Składnik)

from .models import Skład
admin.site.register(Skład)
