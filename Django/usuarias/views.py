from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro
from .forms import Cadastrodenuncias

def cadastro_denuncias(request):
    form = Cadastrodenuncias(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'cadastro_denuncia.html', {'form': form})