from django.urls import path
from app_projeto_user import views
from django.contrib import admin

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path("", views.home, name="home"),
    path("usuarios/", views.usuarios, name="listagem_usuarios"),
    path('cadastro/', view=views.cadastro, name="cadastro"),
    path('login/', view=views.login, name="login"),
    path('admin/', admin.site.urls),
    path('plataforma/', view=views.plataforma, name="plataforma")
]
