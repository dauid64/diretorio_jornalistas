from django import forms
from apps.jornalistas.models import Jornalista
from apps.opcoes.models import Cidades, Estados
from django.core.exceptions import ValidationError


class JornalistaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(JornalistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Jornalista
        fields = [
            'minibio',
            'cidade',
            'estado',
            'funcao',
            'foto',
            'nome_de_guerra',
            'nome',
            'sobrenome',
            'data_de_nascimento',
            'genero',
            'ddi',
            'telefone',
            'cpf',
            'estado_civil',
            'associacoes',
            'registro',
            'curriculo',
            'show_nome_de_guerra',
            'show_nome',
            'show_sobrenome',
            'show_associacoes',
            'show_cpf',
            'show_data_de_nascimento',
            'show_ddi',
            'show_telefone',
            'show_genero',
            'show_estado_civil',
            'show_registro',
            'show_funcao',
            'show_estado',
            'show_cidade'
        ]

        labels = {
            'minibio':'Minibio',
            'cidade':'Cidade Natal',
            'estado':'Estado',
            'show_funcao':'show_funcao',
            'funcao':'Função',
            'foto':'foto',
            'cpf': 'CPF',
            'genero': 'Gênero',
            'registro': 'MTb',
            'associacoes': 'Associações',
            'ddi': 'DDI',
            'curriculo': 'Currículo'
        }

        help_texts = {
            'registro': '''
            Se tem o registro profissional, insira aqui
            ''',
            'curriculo': '''
                Faça o upload de um arquivo no formato PDF.
            '''
        }

        widgets = {

            'minibio': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'id':''
                }
            ),
            'cidade': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class':' form-control'
                }
            ),
            'funcao': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':'',
                }
            ),

            'foto': forms.FileInput(
                attrs={
                    'class': '',
                    'id':'input_profile_photo'
                }
            ),
            'associacoes': forms.SelectMultiple(
                attrs={
                    'class': 'select2 form-control'
                }
            ),
            'nome_de_guerra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'sobrenome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'ddi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'data_de_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado_civil': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'curriculo': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'curriculo_id'
                }
            ),
            'show_nome_de_guerra': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_nome': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_sobrenome': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_associacoes': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_cpf': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_data_de_nascimento': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_ddi': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_telefone': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_genero': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_estado_civil': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_registro': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_funcao': forms.CheckboxInput(
                attrs ={
                    'class':'form-check-input'
                }
            ),
             'show_estado': forms.CheckboxInput(
                attrs ={
                    'class':'form-check-input'
                }
            ),
              'show_cidade': forms.CheckboxInput(
                attrs ={
                    'class':'form-check-input'
                }
            ),
        }


    def clean_telefone(self):
        data = self.cleaned_data['telefone']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )

        return data

    def clean_cpf(self):
        data = self.cleaned_data['cpf']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )
        
        return data

    def clean_ddi(self):
        data = self.cleaned_data['ddi']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )

        return data
