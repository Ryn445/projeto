from django.db import models

class Advogado(models.Model):
    nome = models.CharField(max_length=100)
    oab = models.CharField(max_length=20, unique=True)
    especializacao = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
