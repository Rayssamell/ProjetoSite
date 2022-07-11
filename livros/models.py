from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome 

class Livro(models.Model):

    SERIEALVO_CHOICES = (
    ('1ano', ' 1ano'),
    ('2ano', '2ano'),
    ('3ano', '3ano'),
    )

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    editora = models.CharField(max_length=100)
    anoPublicacao = models.IntegerField()
    isbn = models.CharField(max_length=20)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING, verbose_name="Disciplina") 
    quantidade = models.IntegerField(default='')
    serieAlvo = models.CharField(max_length=8, choices=SERIEALVO_CHOICES, blank=True, null=False)
    imagem = models.ImageField(upload_to='media/', blank=True)
    
    class Meta:
        verbose_name = 'Livros Didáticos'

    def __str__(self):
        return self.titulo

class Emprestimos(models.Model):
    LOAN_STATUS = (
        ('d', 'Disponivel'),
        ('a', 'Agendado'),
        ('s', 'Solicitado'),
        ('e', 'Emprestado'),
    )

    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT, null=True)
    due_back = models.DateTimeField(auto_now=True)
    nome_emprestado = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank = True, null = True)
    nome_emprestado_anonimo = models.CharField(max_length = 30, blank = True, null = True)
    avaliacao = models.CharField(max_length=11, choices=LOAN_STATUS, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"
  
