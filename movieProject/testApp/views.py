from django.shortcuts import render
from testApp.forms import MovieForm
from testApp.models import Movie


# Create your views here.


def index_view(request):
    return render(request, 'testApp/index.html')


def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return index_view(request)
    return render(request, 'testApp/addmovie.html', {'form': form})


def list_movie_view(request):
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request, 'testapp/listmovie.html', {'movies_list': movies_list})
