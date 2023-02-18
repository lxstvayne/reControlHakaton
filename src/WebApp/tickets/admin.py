from django.contrib import admin
from . import models


@admin.register(models.TicketStatus)
class TicketStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class TaskStatusAdmin(admin.ModelAdmin):
    pass
