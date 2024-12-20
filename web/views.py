from django.shortcuts import render,get_list_or_404
from .models import Producto,Categoria
# Create your views here.
"""VISTAS PARA EL CATALOGO PRODUCTOS"""

def index(request):
    listaProductos = Producto.objects.all()
    listaCategoria = Categoria.objects.all()
    
    context = {
        'productos' : listaProductos,
        'categorias' : listaCategoria
    }
    return render(request,'index.html',context)

def productosPorCategoria(request,categoria_id):
    """vista para filtrar por categoria"""
    
    obCaterogira = Categoria.objects.get(pk=categoria_id)
    listaProductos = obCaterogira.producto_set.all()
    
    listaCategorias = Categoria.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    
    return render(request,'index.html',context)

def productosPorNombre(request):
    """vista para filtrar por nombre"""
    
    nombre = request.POST['nombre']
    
    listaProductos = Producto.objects.filter(nombre__contains=nombre) #trae los productos que contengan el nombre
    listaCategorias = Categoria.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    
    return render(request,'index.html',context)
 
 
def productoDetalle(request,producto_id):
    """vista para mostrar el detalle de un producto"""
    obProducto = Producto.objects.get(pk=producto_id)
    obProducto = get_list_or_404(Producto,pk=producto_id)
    context = {
        'producto':obProducto
    } 
    return render(request,'producto.html',context)
     