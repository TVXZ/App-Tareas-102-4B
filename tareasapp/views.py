from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        
        try:
            serializer.save(usuario=self.request.user)
        except Exception:
            serializer.save()



def inicio(request):
    return render(request, 'inicio.html')

def crear_tarea(request):
    return render(request, 'crear.html')

def detalle_tarea(request, id):
    return render(request, 'detalle.html', {'id': id})

def editar_tarea(request, id):
    return render(request, 'editar.html', {'id': id})

def eliminar_tarea(request, id):
    return render(request, 'eliminar.html', {'id': id})

def login_pagina(request):
    return render(request, 'login.html')