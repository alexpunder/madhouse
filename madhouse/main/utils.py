from celery import shared_task
from django.conf import settings
from django.contrib import messages
from telegram import Bot

bot = Bot(token=settings.BOT_TOKEN)


@shared_task()
def send_telegram_message(**kwargs):
    """
    Отправка сообщения в группу организации от имени телеграм-бота.
    """
    name = kwargs.get('name')
    phone = kwargs.get('phone_number')
    text = kwargs.get('message')
    message = (
        'Новый запрос от пользователя. \n\n'
        f'Имя: {name} \n'
        f'Телефон: {phone} \n'
        'Текст обращения: \n'
        f'{text}'
    )
    bot.send_message(chat_id=settings.CHANNEL_ID, text=message)


def generate_error_messages(request, form):
    """Формирует сообщения об ошибках формы в заголовке страницы."""
    for field, errors in form.errors.items():
        if field not in ('reCAPTCHA', 'nickname'):
            field_verbose_name = form._meta.model._meta.get_field(
                field
            ).verbose_name
            for error in errors:
                messages.error(request, f'{field_verbose_name}: {error}')
        else:
            messages.error(request, f'{field}: Ошибка проверки')
