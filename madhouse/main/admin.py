from django.contrib import admin

from .models import SignUp, MainData, Service, ServiceExample


@admin.register(MainData)
class MainDataAdin(admin.ModelAdmin):
    pass


@admin.register(SignUp)
class SignUpAdin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdin(admin.ModelAdmin):
    pass


@admin.register(ServiceExample)
class ServiceExampleAdin(admin.ModelAdmin):
    pass
