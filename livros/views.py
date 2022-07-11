from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from matplotlib.style import context
from django.contrib.auth.decorators import login_required


from django.views.decorators.http import require_POST

from livros.forms import LivroForm

from .models import Emprestimos, Livro

def principal(request):
    return render(request, 'index.html')

@login_required
def meusLivros(request):
    emprestado = User.objects.get(pk = request.user.id)
    livros = Emprestimos.objects.filter(avaliacao= emprestado )
    context = {
        'livros': list(livros),
    }
    return render(request, 'meuslivros.html', context)

@login_required
def agendados(request):
    return render(request, 'agendados.html')

@login_required
def devolvidos(request):
    return render(request, 'devolvidos.html')

@login_required
def buscar_livro(request):
    search = request.GET.get('search')
    if search:
        livros = Livro.objects.filter(titulo__contains=search)
    elif search:
        livros = Livro.objects.filter(disciplina_contains=search)
    
    return render(request, 'livraria/listar_livros.html', {'livros':livros})

@login_required
def listar_livros(request):
    filter = request.GET.get('filter')
    if filter:
        livros = Livro.objects.filter(serieAlvo = filter)
    else:    
        livros = Livro.objects.all()
    return render(request, 'livros/listar_livros.html', {'livros': livros})

@login_required
def listar(request):
    filter = request.GET.get('filter')
    if filter:
        livros = Livro.objects.filter(serieAlvo = filter)
    else:    
        livros = Livro.objects.all()
    return render(request, 'livros/listar.html', {'livros': livros})

@login_required
def detail(request, id):
    livros = Livro.objects.get(pk=id)
    context = {
        "livros": livros
    }
    return render(request, 'livros/detail.html', context)

@login_required
def criar(request):
    
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/livros/listar")
    else:
        form = LivroForm()
    
    context ={
        'form': form
    }
    
    return render(request, "livros/formCriar.html", context)

@login_required
def excluir(request, id):
    
    Livro.objects.get(pk=id).delete()
    
    return HttpResponseRedirect("/livros/listar")    

@login_required
def editar(request, id):
    livros = Livro.objects.get(pk=id)
    
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livros)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/livros/listar")
    else:
        form = LivroForm(instance=livros)
    
    context ={
        'form': form,
        'id': id
    }
    
    return render(request, "livros/formEditar.html", context)



