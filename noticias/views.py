from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Noticia


def inicio(request):

    busca = request.GET.get(
        "q",
        ""
    ).strip()


    todas_noticias = Noticia.objects.filter(
        status="publicado"
    ).order_by(
        "-data_publicacao"
    )


    if busca:

        noticias = todas_noticias.filter(

            Q(titulo__icontains=busca)

            | Q(resumo__icontains=busca)

            | Q(texto__icontains=busca)

            | Q(categoria__icontains=busca)

        )

        destaque = None

        titulo_secao = (
            f'Resultados para "{busca}"'
        )


    else:

        destaque = todas_noticias.first()

        noticias = todas_noticias[1:]

        titulo_secao = "Últimas notícias"


    paginador = Paginator(
        noticias,
        6
    )

    numero_pagina = request.GET.get(
        "page"
    )

    pagina = paginador.get_page(
        numero_pagina
    )


    if pagina.number != 1:

        destaque = None


    return render(
        request,
        "noticias/index.html",
        {
            "destaque": destaque,
            "pagina": pagina,
            "titulo_secao": titulo_secao,
            "busca": busca,
        }
    )


def categoria(
    request,
    nome_categoria
):

    noticias = Noticia.objects.filter(
        status="publicado",
        categoria__iexact=nome_categoria
    ).order_by(
        "-data_publicacao"
    )


    paginador = Paginator(
        noticias,
        6
    )

    numero_pagina = request.GET.get(
        "page"
    )

    pagina = paginador.get_page(
        numero_pagina
    )


    return render(
        request,
        "noticias/index.html",
        {
            "destaque": None,
            "pagina": pagina,
            "titulo_secao": nome_categoria,
            "busca": "",
        }
    )


def detalhe_noticia(
    request,
    id
):

    noticia = get_object_or_404(
        Noticia,
        id=id,
        status="publicado"
    )


    return render(
        request,
        "noticias/detalhe.html",
        {
            "noticia": noticia
        }
    )