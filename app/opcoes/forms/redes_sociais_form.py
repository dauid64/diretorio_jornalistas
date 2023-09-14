from django import forms


class RedesSociaisForm(forms.Form):
    link_telegram = forms.CharField(
        required=False,
        label='Telegram',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    link_facebook = forms.CharField(
        required=False,
        label='Facebook',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    link_podcast = forms.CharField(
        required=False,
        label='Podcast',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    link_linkedin = forms.CharField(
        required=False,
        label='Linkedin',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    link_twitter = forms.CharField(
        required=False,
        label='Twitter',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    link_site = forms.CharField(
        required=False,
        label='Site',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )