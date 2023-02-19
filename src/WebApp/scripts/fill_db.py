import django
django.setup()

from django.contrib.auth.hashers import (
    make_password,
)

from users.models import User, Profession
from tickets import models


def fill():
    fill_user_professions()
    fill_users()
    fill_ticket_statuses()
    fill_task_statuses()
    fill_tickets()
    fill_tasks()


def fill_user_professions():
    professions = [
        Profession(name="Электрик"),
        Profession(name="Сантехник"),
        Profession(name="Отделочник"),
        Profession(name="Клиннер"),
        Profession(name="Инженер"),
    ]

    for prof in professions:
        try:
            prof.save()
        except Exception as e:
            print(e)


def fill_users():
    users = [
        User(
            email="admin@re-control.com",
            phone="88005553535",
            password=make_password("1234"),
            is_superuser=True,
            is_staff=True,
            role=User.RoleChoices.ADMIN
        ),
        User(
            email="test1@re-control.com",
            phone="78005553535",
            password=make_password("1234"),
            fio="Сергей Повелко",
            role=User.RoleChoices.WORKER,
            profession=Profession.objects.get(name="Электрик")
        ),
        User(
            email="test2@re-control.com",
            phone="68005553535",
            password=make_password("1234"),
            fio="Александр Левченко",
            role=User.RoleChoices.WORKER,
            profession=Profession.objects.get(name="Сантехник")
        ),
        User(
            email="test3@re-control.com",
            phone="58005553535",
            password=make_password("1234"),
            fio="Павел Назаров",
            role=User.RoleChoices.WORKER,
            profession=Profession.objects.get(name="Клиннер")
        ),
        User(
            email="test4@re-control.com",
            phone="48005553535",
            password=make_password("1234"),
            fio="Дмитрий Перышкин",
            role=User.RoleChoices.WORKER,
            profession=Profession.objects.get(name="Инженер")
        ),
    ]

    for user in users:
        try:
            user.save()
        except Exception as e:
            print(e)


def fill_ticket_statuses():
    statuses = [
        "Ожидание",
        "Завершено",
        "В процессе",
        "Отменено"
    ]

    for status in statuses:
        try:
            models.TicketStatus(name=status).save()
        except Exception as e:
            print(e)


def fill_task_statuses():
    statuses = [
        "Запланировано",
        "Согласовано",
        "В процессе",
        "На проверке",
        "Отменено",
        "Завершено"
    ]

    for status in statuses:
        try:
            models.TaskStatus(name=status).save()
        except Exception as e:
            print(e)


def fill_tickets():
    tickets = [
        models.Ticket(
            title="Заменить счётчик",
            owner=User.objects.get(email="admin@re-control.com"),
            description="Очень длинное и полезное описание...",
            status=models.TicketStatus.objects.get(name="Ожидание"),
        ),
        models.Ticket(
            title="Ремонт кондиционера",
            owner=User.objects.get(email="admin@re-control.com"),
            description="Очень длинное и полезное описание...",
            status=models.TicketStatus.objects.get(name="Ожидание"),
        ),
        models.Ticket(
            title="Заменить лампочку",
            owner=User.objects.get(email="admin@re-control.com"),
            description="Очень длинное и полезное описание...",
            status=models.TicketStatus.objects.get(name="Ожидание"),
        ),
        models.Ticket(
            title="Поддерживающая уборка",
            owner=User.objects.get(email="admin@re-control.com"),
            description="Очень длинное и полезное описание...",
            status=models.TicketStatus.objects.get(name="Ожидание"),
        )
    ]

    for ticket in tickets:
        try:
            ticket.save()
        except Exception as e:
            print(e)


def fill_tasks():
    tasks = [
        models.Task(
            ticket_id=1,
            query="Заменить счётчик",
            address="Селезнева, д. 7, п. 5, эт. 4., кв. 195.",
            waiting_for=Profession.objects.get(name="Электрик"),
            executor=User.objects.get(email="test1@re-control.com"),
            status=models.TaskStatus(name="Запланировано"),
        ),
        models.Task(
            ticket_id=2,
            query="Ремонт кондиционера",
            address="Селезнева, д. 7, п. 5, эт. 4., кв. 195.",
            waiting_for=Profession.objects.get(name="Инженер"),
            executor=User.objects.get(email="test4@re-control.com"),
            status=models.TaskStatus(name="Запланировано")
        ),
        models.Task(
            ticket_id=3,
            query="Заменить лампочку",
            address="Селезнева, д. 7, п. 5, эт. 4., кв. 195.",
            waiting_for=Profession.objects.get(name="Электрик"),
            executor=User.objects.get(email="test1@re-control.com"),
            status=models.TaskStatus(name="Запланировано"),
        ),
        models.Task(
            ticket_id=4,
            query="Поддерживающая уборка",
            address="Селезнева, д. 7, п. 5, эт. 4., кв. 195.",
            waiting_for=Profession.objects.get(name="Клиннер"),
            executor=User.objects.get(email="test3@re-control.com"),
            status=models.TaskStatus(name="Запланировано"),
        )
    ]

    for task in tasks:
        try:
            task.save()
        except Exception as e:
            print(e)

