from django.contrib import admin

from .models import Livro, Disciplina, Emprestimos

admin.site.register(Livro)
admin.site.register(Disciplina)
admin.site.register(Emprestimos)
