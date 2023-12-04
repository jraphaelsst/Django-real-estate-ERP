from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *



@login_required(login_url='/auth/login')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')
    
    imoveis = Imovei.objects.all()
    cidades = Cidade.objects.all()
    
    if preco_minimo or preco_maximo or tipo or cidade:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 99999999
        if not tipo:
            tipo = ['A', 'C']
            
        imoveis = Imovei.objects.filter(valor__gte=preco_minimo)\
            .filter(valor__lte=preco_maximo)\
                .filter(tipo_imovel__in=tipo)\
                    .filter(cidade=cidade)
        
    else:
        imoveis = Imovei.objects.all()
    
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})


def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestoes': sugestoes})


def agendar_visita(request):
    usuario = request.user
    dia = request.POST.get('dia')
    horario = request.POST.get('horario')
    id_imovel = request.POST.get('id_imovel')
    
    visita = Visita(
        imovel_id = id_imovel,
        usuario = usuario,
        dia = dia,
        horario = horario,
    )
    visita.save()
    return redirect('/agendamentos')


def agendamentos(request):
    visitas = Visita.objects.filter(usuario=request.user)
    return render(request, 'agendamentos.html', {'visitas': visitas})


def finalizar_agendamento(request, id):
    visitas = get_object_or_404(Visita, id=id)
    visitas.status = "F"
    visitas.save()
    return redirect('/agendamentos')


def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visita, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect('/agendamentos')


def apagar_agendamento(request, id):
    visitas = get_object_or_404(Visita, id=id)
    visitas.delete()
    return redirect('/agendamentos')