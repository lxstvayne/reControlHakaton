from django.db import models
from django.utils import timezone

from users.models import User, Profession


class TicketStatus(models.Model):
    name = models.CharField(max_length=48, primary_key=True)

    class Meta:
        db_table = 'kanban_ticket_statuses'


class Ticket(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    owner = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    description = models.TextField()

    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    # set in view when all task statuses changed to "DONE"
    closed_date = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'kanban_tickets'


class TaskStatus(models.Model):
    name = models.CharField(max_length=48, primary_key=True)

    class Meta:
        db_table = 'kanban_task_statuses'


class Task(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='tasks')
    query = models.TextField(null=False, blank=False)

    address = models.CharField(max_length=300, null=True, blank=False)

    # Определяет для какого типа рабочего назначается задача, для дальнейшего распределения в системе.
    waiting_for = models.ForeignKey(Profession, on_delete=models.CASCADE)
    # Выбранный системой исполнитель.
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kanban_tasks'


class FollowUp(models.Model):
    """
    FollowUp это комментарий к таску.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='follow_ups')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    date = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'kanban_task_follow_ups'
