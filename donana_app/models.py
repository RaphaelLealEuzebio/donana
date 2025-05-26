from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image



#Modelo de criação: tabela Categoria.
class Categoria (models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

#Modelo de criação: tabela produtos.

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField( upload_to='donana_app', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagem:
            img_path = self.imagem.path
            img = Image.open(img_path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)


#Modelo de criação: tabela Usuario.

class Usuario (AbstractUser):
    # Campos que já vêm com AbstractUser:
    # username (nome de usuário para login)
    # email
    # first_name (nome)
    # last_name (sobrenome)
    # password (o hash da senha, você não define esse campo diretamente!)
    # is_active, is_staff, is_superuser, date_joined, last_login

    # Adicione seus campos personalizados aqui:
    #data_nascimento = models.DateField(null=True, blank=True)
    # Você pode adicionar outros campos como endereço, telefone, etc.
    # endereco = models.CharField(max_length=200, blank=True)
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
    
#Modelo de criação: tabela Endereço.

class Endereco (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)

#Modelo de criação: tabela Carrinho.
class Carrinho (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='carrinhos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True) 
    finalizado = models.BooleanField(default=False)
    def __str__(self):
        return f"Carrinho #{self.id} - {self.usuario.nome}"
    @property
    def total (self):
        return sum(item.subtotal() for item in self.itemCarrinho.all())

#Modelo de criação: tabela ItemCarrinho.
class ItemCarrinho (models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE,related_name='itens_carrinhos')
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE,related_name='produtos')
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Carrinho{self.carrinho})"
    
    def save(self,*args, **kwargs):
        if not self.preco:
            self.preco = self.produto.preco
        super().save(*args, **kwargs)
    
    def subtotal (self):
        return self.preco * self.quantidade