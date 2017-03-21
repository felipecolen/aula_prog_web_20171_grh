"""grh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app_pessoa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # aqui são as urls do ADMIN, não precisa alterar nada aqui

    url(r'^$', views.index),  #é a url referente a "raiz" do sistema o /, ex: localhost:8000/
    url(r'^index/', views.index, name='index'),  # corresponde a localhost:8000/index
    url(r'^pessoa/', views.mostrapessoa),
    url(r'^contratos/', views.mostrarcontrato),


    # url(r'^index/', views., name='pessoa'),
    # url(r'^index/', views.index, name='index'),

]
