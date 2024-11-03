from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .forms import SignUpForm
from .utils import generate_error_messages
from .models import MainData, Service, ServiceExample


def index(request):
    main_data = MainData.objects.first()
    services = main_data.service_set.all()
    examples = main_data.serviceexample_set.all()

    context = {
        'main_data': main_data,
        'services': services,
        'examples': examples,
        'form': SignUpForm(),
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request=request,
                message=(
                    'Сообщение успешно отправлено! '
                    'В ближайшее время мы с Вами свяжемся.'
                )
            )
            return render(
                request=request,
                template_name='main.html',
                context=context,
            )
        else:
            generate_error_messages(
                request=request,
                form=form,
            )
            return redirect(f'{request.path}#section-contact')

    return render(
        request=request,
        template_name='main.html',
        context=context,
    )


def example_page(request, example_id):
    example = get_object_or_404(ServiceExample, id=example_id)
    return render(
        request=request,
        template_name='example_page.html',
        context={'example_page': example},
    )


def service_page(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(
        request=request,
        template_name='service_page.html',
        context={'service_page': service},
    )
