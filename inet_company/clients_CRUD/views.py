from django.shortcuts import render
from django.views.generic import ListView
from clients_CRUD.models import Client

# Create your views here.

class ClientList(ListView):
    model=Client
    template_name='clients_CRUD/index.html'