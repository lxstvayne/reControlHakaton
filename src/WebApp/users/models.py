from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phone_field import PhoneField


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password, **kwargs):
        if email is None:
            raise TypeError('Users must have a email.')

        if phone is None:
            raise TypeError('Users must have a phone.')

        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, **kwargs):
        user = self.create_user(email, **kwargs)
        user.is_superuser = True
        user.save()
        return user


class Profession(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, unique=True)
    phone = PhoneField(null=False, unique=True)

    # Обязательное поле если нужно использовать админку джанго
    is_staff = models.BooleanField(default=False)

    fio = models.CharField(max_length=255, null=True, blank=False)
    photo = models.ImageField(upload_to='photos/', null=True, max_length=255)
    organization = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)

    # На проде будет больше ролей
    class RoleChoices(models.TextChoices):
        ADMIN = 'Администратор'
        WORKER = 'Рабочий'
        GUEST = 'Гость'

    role = models.CharField(
        max_length=32,
        choices=RoleChoices.choices,
        default=RoleChoices.GUEST,
        null=False
    )

    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'
