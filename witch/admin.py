from django.contrib import admin
from .models import Service, Comment, Certificate, AdditionalText


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class AdditionalTextInline(admin.TabularInline):
    model = AdditionalText
    extra = 1


class ServiceAdmin(admin.ModelAdmin):
    inlines = [CommentInline, AdditionalTextInline]


admin.site.register(Service, ServiceAdmin)
admin.site.register(Certificate)
