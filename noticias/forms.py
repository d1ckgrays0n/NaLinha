from django import forms

from .models import Noticia


class NoticiaAdminForm(forms.ModelForm):

    class Meta:
        model = Noticia

        fields = "__all__"

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Digite o título da notícia"
                }
            ),

            "resumo": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Escreva um resumo curto da notícia"
                }
            ),

            "texto": forms.Textarea(
                attrs={
                    "rows": 20,
                    "placeholder": "Escreva a matéria completa aqui"
                }
            ),
        }