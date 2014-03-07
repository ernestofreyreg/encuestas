from django.contrib import admin

# Register your models here.
from enc.models import Encuesta, Imagen


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('nombre','vigente')

admin.site.register(Encuesta, EncuestaAdmin)

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('imageurl', 'id', 'archivo')

admin.site.register(Imagen, ImagenAdmin)