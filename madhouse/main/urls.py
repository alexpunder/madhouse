from django.urls import path

from .views import example_page, index, service_page

app_name = 'main'

urlpatterns = [
    path('', index, name='indexpage'),
    path('examples/<int:example_id>', example_page, name='example_page'),
    path('services/<int:service_id>', service_page, name='service_page'),
]
