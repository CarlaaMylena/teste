from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Filme(models.Model):
    nome_filme = models.CharField(max_length=250)
    ano = models.IntegerField()
    diretores = models.CharField(max_length=80)

    def __str__(self):
        return self.nome_filme