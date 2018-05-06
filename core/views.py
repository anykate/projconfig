from django.views.generic import ListView
from .models import Movie


# Create your views here.
class MovieListView(ListView):
    model = Movie
    template_name = 'core/index.html'
    context_object_name = 'movies'
    # ordering = ['year']
