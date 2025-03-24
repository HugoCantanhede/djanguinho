from django.contrib import admin

from sistema import models

# Register your models here.

@admin.register(models.Usuário)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome' ,'email','ativo',)

    
