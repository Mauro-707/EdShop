from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT) 
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    imagen = models.ImageField(upload_to='productos', blank=True)
    
    

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

 