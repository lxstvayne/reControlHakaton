from django.contrib import admin
from . import models


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
