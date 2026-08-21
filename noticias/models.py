from django.db import models


class Noticia(models.Model):

    CATEGORIAS = [
        ("Futebol", "Futebol"),
        ("NBA", "NBA"),
        ("Games", "Games"),
    ]


    STATUS = [
        ("rascunho", "Rascunho"),
        ("publicado", "Publicado"),
    ]


    titulo = models.CharField(
        max_length=200
    )


    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS
    )


    resumo = models.TextField()


    texto = models.TextField()


    imagem = models.ImageField(
        upload_to="noticias/",
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="publicado"
    )


    data_publicacao = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.titulo