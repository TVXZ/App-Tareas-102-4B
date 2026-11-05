from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from tareasapp.views import (
    TareaViewSet, 
    inicio, 
    crear_tarea, 
    detalle_tarea, 
    editar_tarea, 
    eliminar_tarea, 
    login_pagina
)

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    path('inicio/', inicio, name='inicio'),
    path('login/', login_pagina, name='login'),
    path('crear/', crear_tarea, name='crear_tarea'),
    path('detalle/<int:id>/', detalle_tarea, name='detalle'),
    path('editar/<int:id>/', editar_tarea, name='editar'),
    path('eliminar/<int:id>/', eliminar_tarea, name='eliminar'),
    
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    
    path('api/v1/', include(router.urls)),
]