from django.contrib import admin
from .models import Cliente, Telefone, CPF, Departamentos


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos', )
    search_fields = ('id', 'nome')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamentos)