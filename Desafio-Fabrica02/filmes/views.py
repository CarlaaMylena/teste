from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme, Diretor
from .forms import FilmeForm
import requests

def listar_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/listar_filmes.html', {'filmes': filmes})

def criar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm()
    return render(request, 'filmes/form_filmes.html', {'form': form})

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'filmes/form_filme.html', {'form': form})

def deletar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('listar_filmes')
    return render(request, 'filmes/confirmar_exclusao.html', {'filme': filme})

def buscar_filme_omdb(request):
    titulo = request.GET.get('titulo')
    if titulo:
        api_key = "d9eb6970"
        url = f"http://www.omdbapi.com/?i=tt3896198&apikey=d9eb6970"
        response = requests.get(url)
        data = response.json()
        return render(request, 'filmes/buscar_filme.html', {'filme': data})
    return render(request, 'filmes/buscar_filme.html')