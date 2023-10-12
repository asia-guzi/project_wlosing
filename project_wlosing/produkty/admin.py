from django.contrib import admin

# Register your models here.


from .models import Kosmetyk
admin.site.register(Kosmetyk)

from .models import Szampon
admin.site.register(Szampon)

from .models import Odżywka
admin.site.register(Odżywka)

from .models import Maska
admin.site.register(Maska)

from .models import Olejek
admin.site.register(Olejek)

from .models import Olej
admin.site.register(Olej)

from .models import Żel
admin.site.register(Żel)

from .models import Pianka
admin.site.register(Pianka)

from .models import Krem
admin.site.register(Krem)

from .models import Wcierka
admin.site.register(Wcierka)

from .models import Peeling
admin.site.register(Peeling)

from .models import Rdz
admin.site.register(Rdz)