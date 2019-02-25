from django.views.generic import ListView, DetailView
from .models import Movie
from django.shortcuts import render


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


def server_error(request):
    return render(request, '404.html')


def not_found(request):
    return render(request, '404.html')
