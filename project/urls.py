"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_sys_ICCN import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path("<int:server_id>",views.server, name='server'),
    path("ramdisk<int:server_id>",views.ramdisk,name="ramdisk"),
    path('Gestion_serveur', views.Gestion_serveur, name='Gestion_serveur'),
    path('Gestion_utilisateur', views.Gestion_utilisateur, name='Gestion_utilisateur'),
    path('modifier_serveur', views.modifier_serveur, name='modifier_serveur'),
    path('ajouter_serveur', views.ajouter_serveur, name='ajouter_serveur'),
    path('modifier_utilisateur', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('ajouter_utilisateur', views.ajouter_utilisateur, name='ajouter_utilisateur'),
]
