from django.contrib import admin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin

from .models import MainData, Service, ServiceExample, SignUp, Certificate

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(MainData)
class MainDataAdmin(ModelAdmin):
    list_display = (
        'title',
        'phone',
    )


@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    pass


@admin.register(SignUp)
class SignUpAdmin(ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'name',
        'phone_number',
    )


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(ServiceExample)
class ServiceExampleAdmin(ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'client',
        'service_type',
    )
