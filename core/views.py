from django.shortcuts import render
from .models import Usuarios


def index(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})
