from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.inicio,
        name="inicio"
    ),

    path(
        "categoria/<str:nome_categoria>/",
        views.categoria,
        name="categoria"
    ),

    path(
        "noticia/<int:id>/",
        views.detalhe_noticia,
        name="detalhe_noticia"
    ),

]