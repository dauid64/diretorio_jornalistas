from django import forms
from jornalistas.models import HistoricoProfissional
from django.core.exceptions import ValidationError


class HistoricoForm(forms.ModelForm):
    cargo_atual = forms.BooleanField(
        required=False,
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

        help_texts = {
            'referencia': '''
            Nos campos de referência e contato você deve informar o nome e algum meio para se comunicar com a pessoa responsável ao cargo, para que possamos confirmar sua participação nesse cargo
            '''
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
    
    def clean(self):
        cleaned_data = super().clean()
        cargo_atual = cleaned_data.get('cargo_atual', False)
        data_de_termino = cleaned_data.get('data_de_termino', None)
        if cargo_atual is False and data_de_termino is None:
            raise ValidationError({
                "data_de_termino": "Marque a opção cargo atual ou insira uma data final do cargo"
            })
        return cleaned_data