# Generated by Django 4.2.5 on 2023-10-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Katergorianer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anun', models.CharField(max_length=60, verbose_name='Kategoriayi anuny')),
            ],
        ),
        migrations.CreateModel(
            name='EntaKategorianer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anun', models.CharField(max_length=60, verbose_name='EntaKategoria anun')),
                ('gin', models.PositiveIntegerField(verbose_name='Entakategoria gin')),
                ('kategorian', models.ManyToManyField(to='main.katergorianer')),
            ],
        ),
    ]
