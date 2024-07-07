from django.forms import ModelForm
from .models import *

class CadastroForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'turma']