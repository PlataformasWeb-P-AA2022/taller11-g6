from django.contrib import admin

from administrativo.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad', 'tipo')


admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'costo', 'numCuartos', 'edificio')
    search_fields = ('propietario', 'costo', 'numCuartos', 'edificio')

    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)