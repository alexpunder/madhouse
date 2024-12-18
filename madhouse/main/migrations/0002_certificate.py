# Generated by Django 5.1.2 on 2024-11-08 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название сертификата')),
                ('description', models.TextField(verbose_name='Описание сертификата')),
                ('image', models.ImageField(help_text='Размер изображений: 700x700', upload_to='certificates', verbose_name='Изображение')),
                ('certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maindata')),
            ],
        ),
    ]
