from django.contrib import admin
from .models import Service, Comment, Certificate, AdditionalText


class AdditionalTextInline(admin.TabularInline):
    model = AdditionalText


class ServiceAdmin(admin.ModelAdmin):
    inlines = [AdditionalTextInline]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Certificate)
admin.site.register(Comment)
