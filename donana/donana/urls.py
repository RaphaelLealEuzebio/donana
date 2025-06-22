from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from donana_app.views import *

router = DefaultRouter()
router.register(r'categoria',CategoriaViewSet)
router.register(r'produtos',ProdutoViewSet)
router.register(r'itemCarrinho',ItemCarrinhoViewSet)
router.register(r'carrinho',CarrinhoViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'usuario',UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
