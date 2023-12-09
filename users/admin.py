from django.contrib import admin

from projects.models import Project
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass
