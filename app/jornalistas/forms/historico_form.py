from django import forms
from jornalistas.models import HistoricoProfissional


class HistoricoForm(forms.ModelForm):
    cargo_atual = forms.BooleanField(
        label='Trabalho atualmente neste cargo',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input historico-checkout',
            }
        )
    )

    class Meta:
        model = HistoricoProfissional
        exclude = ["duracao", "validado", "revisor_responsavel"]
        labels = {
            "veiculo_de_comunicacao": "Veículo de comunicação",
            "cargo": "Cargo",
            "data_inicio": "Data de Início",
            "data_de_termino": "Data de Termino",
            "referencia": "Referência",
            "contato_da_referencia": "Contato de Referência",
            "descricao": "Descrição",
        }

        widgets = {
            "veiculo_de_comunicacao": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "cargo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cargo"
                }
            ),
            "contato_da_referencia": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contato da Referência"
                }
            ),
            "data_inicio": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                },
                format='%d/%m/%Y'
            ),
            "data_de_termino": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Data de Encerramento",
                    "type": "date"
                },
                format='%d/%m/%Y'
            ),
            "referencia": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Referência"
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "form-control span",
                    "placeholder": "Descrição"
                }
            ),
        }