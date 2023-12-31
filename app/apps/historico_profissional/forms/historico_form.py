from django import forms
from apps.historico_profissional.models import HistoricoProfissional
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

    def __init__(self, *args, **kwargs):
        super(HistoricoForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)
        if instance:
            self.fields['cargo_atual'].initial = True if \
                instance.data_termino is None else False

    class Meta:
        model = HistoricoProfissional
        fields = [
            'veiculo_de_comunicacao',
            'tipo_de_veiculo',
            'cargo',
            'cargo_atual',
            'data_inicio',
            'data_termino',
            'descricao'
        ]
        labels = {
            "veiculo_de_comunicacao": "Veículo de comunicação",
            "tipo_de_veiculo": 'Tipo de veículo',
            "cargo": "Cargo",
            "data_inicio": "Data de Início",
            "data_termino": "Data de Termino",
            "descricao": "Descrição",
        }

        widgets = {
            "veiculo_de_comunicacao": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "tipo_de_veiculo": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "cargo": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "data_inicio": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                },
                format='%Y-%m-%d'
            ),
            "data_termino": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                },
                format='%Y-%m-%d'
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
        data_termino = cleaned_data.get('data_termino', None)
        data_inicio = cleaned_data.get('data_inicio', None)
        if cargo_atual is False and data_termino is None:
            raise ValidationError({
                "data_termino": "Marque a opção cargo atual ou insira uma data final do cargo"
            })
        if data_termino is not None and data_inicio > data_termino:
            raise ValidationError({
                'data_termino': 'A data final não pode ser menor que a data de inicio'
            })
        return cleaned_data
