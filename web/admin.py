from django.contrib import admin

# Register your models here.
from .models import Categoria,Producto

admin.site.register(Categoria)
#admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria','fecha_ingreso') # campos q se mostraran en el panel de admin/productos
    #list_editable = ('precio',) # puedes editar el precio