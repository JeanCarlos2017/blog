from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    tituloPost = models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tituloPost