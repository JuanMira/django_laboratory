from django.shortcuts import render, redirect, get_object_or_404
from Movies.models import Categories
from django.forms import ModelForm
from Categorias.forms import CategoriesForm

# Create your views here.

def get_all_categories(request):
    categories = Categories.objects.all()
    return render(request,'categorias_inicio.html',{'categories':categories})
    

def nueva_categoria(request):
    if request.method == 'POST':
        categorie_form = CategoriesForm(request.POST)
        if categorie_form.is_valid():
            categorie_form.save()
            return redirect('categorias')        
    else:
        categorie_form = CategoriesForm()
    return render(request,'nuevo_categorie.html',{'categorie_form':categorie_form})

def editar_categoria(request,id):
    categories = get_object_or_404(Categories, pk=id)
    if request.method == 'POST':
        categorie_form = CategoriesForm(request.POST, instance=categories)
        if categorie_form.is_valid():
            categorie_form.save()
            return redirect('categorias')        
    else:
        categorie_form = CategoriesForm(instance=categories)
    return render(request,'editar_categoria.html',{'categorie_form':categorie_form})

def eliminar_categoria(request,id):
    categories = get_object_or_404(Categories,pk=id)
    if categories:
        categories.delete()
    return redirect('categorias')