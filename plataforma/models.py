from django.db import models
from django.contrib.auth.models import User
from datetime import time


class Imagen(models.Model):
    img = models.ImageField(upload_to='img')
    
    def __str__(self) -> str:
        return self.img.url


class Cidade(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nome


class DiasVisita(models.Model):
    dia = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.dia


class Horario(models.Model):
    horario = models.TimeField()
    
    def __time__(self) -> time:
        return self.horario
    
    
class Imovei(models.Model):
    choices = (
        ('V', 'Venda'),
        ('A', 'Aluguel'),
    )
    
    choices_imoveis = (
        ('A', 'Apartamento'),
        ('C', 'Casa'),
    )
    
    imagens = models.ManyToManyField(Imagen)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imoveis)
    numero = models.IntegerField()
    descricao = models.TextField()
    dias_visita = models.ManyToManyField(DiasVisita)
    horarios = models.ManyToManyField(Horario)
    
    def __str__(self) -> str:
        return self.rua


class Visita(models.Model):
    choices = (
        ('Sg', 'Segunda'),
        ('T', 'Terça'),
        ('Qa', 'Quarta'),
        ('Qi', 'Quinta'),
        ('Sx', 'Sexta'),
        ('Sa', 'Sábado'),
        ('D', 'Domingo'),
    )
    
    choices_status = (
        ('A', 'Agendado'),
        ('F', 'Finalizado'),
        ('C', 'Cancelado'),
    )
    
    imovel = models.ForeignKey(Imovei, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dia = models.CharField(max_length=20)
    horario = models.CharField(max_length=24)
    status = models.CharField(max_length=1, choices=choices_status, default='A')
    
    def __str__(self) -> str:
        return self.usuario.username
