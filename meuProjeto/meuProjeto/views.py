from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    lista = [
        {'nome': 'Rafael', 'sexo': 'm'},
        {'nome': 'Sindy', 'sexo': 'f'},
        {'nome': 'Silas', 'sexo': 'm'},
        {'nome': 'Pedro', 'sexo': 'm'}
    ]
    return render(request, 'index.html', {'lista': lista})

 