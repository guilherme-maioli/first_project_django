from django.shortcuts import render
from .models import User_aula1
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "usuarios/home.html")

def usuarios(request):
    new_user = User_aula1()
    new_user.name = request.POST.get("name")
    new_user.age = request.POST.get("age")
    new_user.save()

    # show all users in new page
    users = {"users": User_aula1.objects.all()}

    return render(request, 'usuarios/usuarios.html', users)

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("ja existe usuario")

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()


        return HttpResponse("usuario cadastrado com sucesso.")

def login(request):
    if request.method == "GET":
        return render(request, 'cadastro/login.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)

            return HttpResponse("autenticado")
        else:
            return HttpResponse("falha")

@login_required(login_url='/login/')       
def plataforma(request):
    return HttpResponse("plataforma.")

