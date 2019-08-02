"""pari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.inscription),
    path('login/', views.connexion),
    path('profile/', views.profile, name='profile'),
    path('mylogin/', views.mylogin, name='mylog'),
    path('mylogout/', views.mylogout, name='mylogout'),
    path('scrap',views.scrap,name='scrap'),
    path('resultat',views.resultat,name='resultat'),
    path('affichage',views.affichage,name='affichage'),
    path('form',views.form,name='form'),
    path('match',views.enregistrer,name='match'),
    path('monpari/<id>',views.monpari,name='monpari'),
]
