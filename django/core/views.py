from django.views.generic import ListView, DetailView
from .models import Movie, Person
from django.shortcuts import render


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    queryset = (Movie.objects.all_with_related_persons())


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

def server_error(request):
    return render(request, '404.html')


def not_found(request):
    return render(request, '404.html')

