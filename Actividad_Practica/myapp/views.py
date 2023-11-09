from django.shortcuts import render
from .models import Categoria, Producto
def index(request):
    title = "inicio"

    data = {
        "title" : title,
        "categorias" : Categoria.objects.all(),
        "productos" : Producto.objects.all()
    }

    return render(request, 'myapp/index.html',data)

def nuevo(request):
    filtro = request.GET.get('Cat')
    prods = Producto.objects.all()
    title = "Inicio"
    categ = None
    if filtro != 'Categorias' and filtro!=None:
        categ = Categoria.objects.filter(category=filtro).first()
        prods = Producto.objects.filter(category=categ)
    data = {
        "title": title,
        "productos" : prods,
        "categorias" : Categoria.objects.all(),
    }
    return render(request, 'myapp/index.html', data)

