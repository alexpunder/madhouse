from django.shortcuts import get_object_or_404, render

from .forms import SignUpForm
from .models import MainData, Service, ServiceExample


def index(request):
    main_data = MainData.objects.first()
    services = main_data.service_set.all()
    examples = main_data.serviceexample_set.all()

    form = SignUpForm()

    context = {
        'main_data': main_data,
        'services': services,
        'examples': examples,
        'form': form,
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return render(
                request=request,
                template_name='main.html',
                context=context,
            )

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
