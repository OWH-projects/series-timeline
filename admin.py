from myproject.projects.models import *
from django.contrib import admin

class InstallmentInline(admin.StackedInline):
    model = Installment
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    ordering = [ '-id', ]
    list_display = ['title', 'slug', 'viewable']
    inlines = [InstallmentInline]

admin.site.register(Project, ProjectAdmin)

