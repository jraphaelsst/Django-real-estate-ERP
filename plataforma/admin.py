from .models import *
from django.contrib import admin


@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Imagen)
admin.site.register(Cidade)
admin.site.register(Visita)