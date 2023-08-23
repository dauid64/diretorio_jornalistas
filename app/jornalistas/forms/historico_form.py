from django import forms
from jornalistas.models import HistoricoProfissional


class HistoricoForm(forms.ModelForm):
    class Meta:
        model = HistoricoProfissional
        exclude = ["duracao", "validado", "revisor_responsavel"]
        labels = {
            "veiculo_de_comunicacao": "veiculo",
            "cargo": "cargo",
            "data_inicio": "Data de Início",
            "data_de_termino": "Data de Termino",
            "referencia": "referência",
            "contato_da_referencia": "Contato de Referência",
            "descricao": "descrição",
        }

        widgets = {
            "veiculo_de_comunicacao": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Veiculo"
                }
            ),
            "cargo": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Cargo"
                }
            ),
            "contato_da_referencia": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Contato da Referência"
                }
            ),
            "data_inicio": forms.DateInput(
                attrs={
                    "class": "form-control2 mask-date",
                    "placeholder": "Data de Inicio"
                }
            ),
            "data_de_termino": forms.DateInput(
                attrs={
                    "class": "form-control2 mask-date",
                    "placeholder": "Data de Encerramento"
                }
            ),
            "referencia": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Referência"
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control2 span",
                    "placeholder": "Descrição"
                }
            ),
        }