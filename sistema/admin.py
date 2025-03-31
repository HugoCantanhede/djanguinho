from django.contrib import admin

from sistema import models

# Register your models here.

@admin.register(models.Usuário)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome' ,'email','ativo','imagem')

    
@admin.register(models.Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ano' , 'estudio','genero','ativo',)


@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)

