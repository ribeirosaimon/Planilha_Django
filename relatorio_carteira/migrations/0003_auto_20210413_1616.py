# Generated by Django 3.1.7 on 2021-04-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio_carteira', '0002_auto_20210413_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrimoniomodel',
            name='vol_br',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='patrimoniomodel',
            name='vol_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='patrimoniomodel',
            name='vol_usa',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]