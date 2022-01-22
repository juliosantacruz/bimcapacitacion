from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Pagina(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    imagen = models.ImageField(verbose_name="Imagen", upload_to="images/paginas", blank=True, null=True)
    contenido = RichTextUploadingField()
    creado = models.DateTimeField(auto_now_add=True)
    publicar = models.BooleanField(default=True)


    def __str__(self):
        return self.titulo

