# Generated by Django 4.0.5 on 2022-06-28 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbookapp', '0003_trade_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mercados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mercado', models.CharField(max_length=250, verbose_name='Watch List')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True, unique=True, verbose_name='Fecha de operacion')),
                ('nota', models.CharField(max_length=250, verbose_name='Notas de trading')),
            ],
        ),
    ]