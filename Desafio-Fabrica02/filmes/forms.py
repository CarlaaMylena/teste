from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class meta:
        model = Filme
        fields = ['nome_filme', 'ano', 'diretores']
        labels = {
        'nome_filme': 'titulo',
        'ano': 'ano',
        'diretores': 'diretores',
        }
        widgets = {
        'nome_filme': forms.TextInput(attrs={'class': 'form-control'}),
        'ano': forms.TextInput(attrs={'class': 'form-control'}),
        'diretores': forms.TextInput(attrs={'class': 'form-control'}),
        }