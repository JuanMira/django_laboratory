from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from Movies.models import Movies
from Movies.forms import MoviesForm

# Create your views here.

def new_movie(request):
    if request.method == 'POST':
        form_movies = MoviesForm(request.POST)
        if form_movies.is_valid():
            form_movies.save()
            return redirect('detail_movies')
    else:
        form_movies = MoviesForm()
    return render(request,'nuevo.html',{'form_movies':form_movies})

def get_all_movies(request):
    movies = Movies.objects.all()
    return render(request,'movies.html',{'movies':movies})

def get_movie(request,id):
    movie = get_object_or_404(Movies,pk=id)
    return render(request,'movie_datail.html',{'movie':movie})

def get_detail_movie(request):
    movie = Movies.objects.all()
    return render(request,'movie_list.html',{'movie':movie})

def edit_movie(request,id):
    movie = get_object_or_404(Movies,pk=id)
    if request.method == 'POST':
        movie_form = MoviesForm(request.POST,instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('detail_movies')
    else:
        movie_form = MoviesForm(instance=movie)
    return render(request,'movie_edit.html',{'movie_form':movie_form})

def delete_movie(request,id):
    movie = get_object_or_404(Movies,pk=id)
    if movie:
        movie.delete()
    return redirect('detail_movies')