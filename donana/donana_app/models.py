from django.db import models
from PIL import Image


class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField( upload_to='donana_app', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagem:
            img_path = self.imagem.path
            img = Image.open(img_path)

            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)

               