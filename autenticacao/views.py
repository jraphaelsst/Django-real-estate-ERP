from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.urls import reverse


def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)
        email = User.objects.filter(email=email)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')
            return redirect(reverse('cadastro'))
        
        if email.exists():
            messages.add_message(request, constants.ERROR, 'Email já cadastrado.')
            return redirect(reverse('cadastro'))

        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect(reverse('cadastro'))
        
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha)
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            user.save()
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema.')
            return redirect('/auth/cadastro')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=username, password=senha)
        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos.')
            return redirect(reverse('login'))
        
        else:
            auth.login(request, user)
            return(redirect('/'))


def logout(request):
    auth.logout(request)
    redirect(reverse('/auth/login'))