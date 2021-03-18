# Generated by Django 3.1.7 on 2021-03-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20210314_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendamodel',
            name='data',
            field=models.DateField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendamodel',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vendamodel',
            name='criacao',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]