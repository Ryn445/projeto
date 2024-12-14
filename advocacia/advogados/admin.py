from django.contrib import admin
from .models import Advogado

@admin.register(Advogado)
class AdvogadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'oab', 'especializacao', 'email')
    search_fields = ('nome', 'oab', 'email')
    list_filter = ('especializacao',)
