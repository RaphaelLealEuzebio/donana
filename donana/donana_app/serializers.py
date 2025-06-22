from rest_framework import serializers

#Importacao de todas as Models
from .models import *

#Importacao da tabela padrao User
from django.contrib.auth.models import User

#serializers Categoria/Produtos (Nested Serializers)
class CategoriaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializers (serializers.ModelSerializer):
    produtos = CategoriaSerializers(read_only = True)
    class Meta:
        model = Produtos
        fields ='__all__'


#serializers ItemCarrinho/Carrinho (Nested Serializers)
class ItemCarrinhoSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = ItemCarrinho
        fields = '__all__'
        
    def get_subtotal(self, obj):
        return obj.subtotal()

class CarrinhoSerializers(serializers.ModelSerializer):
    itens_carrinhos = ItemCarrinhoSerializer(many=True, read_only= True)
    total = serializers.ReadOnlyField()
    class Meta:
        model = Carrinho
        fields = '__all__'

#serializers de Usuarios/Endereço (Nested Serializers)
class EnderecoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
        
class UsuarioSerializers (serializers.ModelSerializer):
    enderecos = EnderecoSerializers(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'

