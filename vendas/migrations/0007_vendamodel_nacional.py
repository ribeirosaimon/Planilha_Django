# Generated by Django 3.1.7 on 2021-03-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_vendamodel_preco_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendamodel',
            name='nacional',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
