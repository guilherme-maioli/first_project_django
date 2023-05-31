from django.shortcuts import render
from .models import User


def home(request):
    return render(request, "usuarios/home.html")


def usuarios(request):
    new_user = User()
    new_user.name = request.POST.get("name")
    new_user.age = request.POST.get("age")
    new_user.save()

    # show all users in new page
    users = {"users": User.objects.all()}

    return render(request, 'usuarios/usuarios.html', users)
