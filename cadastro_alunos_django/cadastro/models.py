from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.turma}" 