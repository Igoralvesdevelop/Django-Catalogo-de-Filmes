from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.shortcuts import render
from .models import Filmes

def lista_filmes(request):
    filmes = Filmes.objects.all
    return render(request, 'filmes/lista.html', {'filmes': filmes})