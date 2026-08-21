from django.contrib import admin

from .forms import NoticiaAdminForm
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):

    form = NoticiaAdminForm


    list_display = (
        "titulo",
        "categoria",
        "status",
        "data_publicacao",
        "data_atualizacao",
    )


    list_filter = (
        "status",
        "categoria",
        "data_publicacao",
    )


    search_fields = (
        "titulo",
        "resumo",
        "texto",
    )


    readonly_fields = (
        "data_publicacao",
        "data_atualizacao",
    )


    fieldsets = (

        (
            "Informações principais",
            {
                "fields": (
                    "titulo",
                    "categoria",
                    "status",
                    "imagem",
                    "resumo",
                )
            },
        ),

        (
            "Matéria",
            {
                "fields": (
                    "texto",
                )
            },
        ),

        (
            "Informações do sistema",
            {
                "fields": (
                    "data_publicacao",
                    "data_atualizacao",
                )
            },
        ),

    )