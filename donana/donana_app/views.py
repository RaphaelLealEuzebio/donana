from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

#ViewsSets : categoria e produtos.
class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ProdutoViewSet (viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutoSerializers

#ViewsSets : ItemCarrinho e Carrinho.
class ItemCarrinhoViewSet (viewsets.ModelViewSet):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer

class CarrinhoViewSet (viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializers

#ViewsSets : Endereco e Usuario
class EnderecoViewSet (viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializers

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializers
 
