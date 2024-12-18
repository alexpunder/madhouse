# Generated by Django 5.1.2 on 2024-11-06 06:24

import datetime
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Нзвание организации')),
                ('about_us', models.TextField(verbose_name='О нас')),
                ('vk', models.CharField(max_length=255, verbose_name='Ссылка на ВКонтакте')),
                ('instagram', models.CharField(max_length=255, verbose_name='Ссылка на Инстаграмм')),
                ('telegram', models.CharField(max_length=255, verbose_name='Ссылка на Телеграм')),
                ('whatsapp', models.CharField(max_length=255, verbose_name='Ссылка на WhatsApp')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер для связи')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Основные данные',
                'verbose_name_plural': 'Основные данные',
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата/время создания')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон пользователя')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Обращения',
                'verbose_name_plural': 'Обращения',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('image', models.ImageField(help_text='Размер изображений: 700x700', upload_to='services', verbose_name='Изображение')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maindata')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServiceExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today, verbose_name='Дата оказания услуги')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('client', models.CharField(max_length=255, verbose_name='Клиент')),
                ('service_type', models.CharField(max_length=255, verbose_name='Тип услуги')),
                ('image', models.ImageField(help_text='Размер изображений: 700x467', upload_to='examples', verbose_name='Изображение')),
                ('service_example', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maindata')),
            ],
            options={
                'verbose_name': 'Пример работы',
                'verbose_name_plural': 'Примеры работ',
            },
        ),
    ]
