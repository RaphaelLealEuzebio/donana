# Generated by Django 5.2 on 2025-06-22 19:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donana_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('finalizado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('Categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='donana_app.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='produtos',
            name='categoria',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='donana_app.categoria'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_carrinhos', to='donana_app.carrinho')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_carrinho', to='donana_app.produtos')),
            ],
        ),
    ]
