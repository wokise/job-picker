from django.contrib import admin
from .models import City, Language, Vacansy, Error, Url

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacansy)
admin.site.register(Error)
admin.site.register(Url)