from django.shortcuts import render

from .models import MainData


def index(request):
    main_data = MainData.objects.first()
    services = main_data.service_set.all()
    examples = main_data.serviceexample_set.all()

    context = {
        'main_data': main_data,
        'services': services,
        'examples': examples,
    }

    return render(
        request=request,
        template_name='main.html',
        context=context,
    )
