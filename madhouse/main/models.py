from datetime import date

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SignUp(models.Model):
    created_at = models.DateTimeField(
        'Дата/время создания',
        auto_now_add=True,
    )
    name = models.CharField(
        'Имя пользователя',
        max_length=255,
    )
    phone_number = PhoneNumberField(
        'Телефон пользователя',
    )
    message = models.TextField(
        'Сообщение',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = [
            '-id',
        ]
        verbose_name = 'Обращения'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'Заявка от {self.name}'


class MainData(models.Model):
    title = models.CharField(
        'Нзвание организации',
        max_length=255,
    )
    about_us = models.TextField(
        'О нас',
    )
    vk = models.CharField(
        'Ссылка на ВКонтакте',
        max_length=255,
    )
    instagram = models.CharField(
        'Ссылка на Инстаграмм',
        max_length=255,
    )
    telegram = models.CharField(
        'Ссылка на Телеграм',
        max_length=255,
    )
    whatsapp = models.CharField(
        'Ссылка на WhatsApp',
        max_length=255,
    )
    phone = PhoneNumberField(
        'Номер для связи',
    )
    adress = models.CharField(
        'Адрес',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Основные данные'
        verbose_name_plural = 'Основные данные'

    def __str__(self):
        return self.title


class Service(models.Model):
    service = models.ForeignKey(
        'MainData',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(
        'Название услуги',
        max_length=255,
    )
    description = models.TextField(
        'Описание услуги',
    )
    image = models.ImageField(
        'Изображение',
        upload_to='services',
        help_text='Размер изображений: 700x700',
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class ServiceExample(models.Model):
    service_example = models.ForeignKey(
        'MainData',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        'Дата оказания услуги',
        default=date.today,
    )
    title = models.CharField(
        'Заголовок',
        max_length=255,
    )
    content = models.TextField(
        'Описание',
    )
    client = models.CharField(
        'Клиент',
        max_length=255,
    )
    service_type = models.CharField(
        'Тип услуги',
        max_length=255,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='examples',
        help_text='Размер изображений: 700x467',
    )

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'

    def __str__(self):
        return self.title
