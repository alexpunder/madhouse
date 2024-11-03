from django.contrib import messages


def generate_error_messages(request, form):
    """Формирует сообщения об ошибках формы в заголовке страницы."""
    for field, errors in form.errors.items():
        if field not in ('reCAPTCHA', 'nickname'):
            field_verbose_name = (
                form._meta.model._meta.get_field(field).verbose_name
            )
            for error in errors:
                messages.error(
                    request, f'{field_verbose_name}: {error}'
                )
        else:
            messages.error(
                request, f'{field}: Ошибка проверки'
            )
