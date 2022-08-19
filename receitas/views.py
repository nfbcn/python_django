from django.shortcuts import render
from .models import Receita


def index(request):

    receitas = Receita.objects.all()
    #print(receitas)
    
    dados = {
        'receitas': receitas
    }
    return render(request,'index.html', dados)

def receita (request, receita_id):
    return render(request, 'receita.html')