from django.urls import path
from .views import cadastro_denuncias

urlpatterns = [
  path('cadastro_denuncias/', cadastro_denuncias ),
]
