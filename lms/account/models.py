from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, image=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            image=image,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
          phone=phone,
          first_name=first_name,
          last_name=last_name,
          password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=12, unique=True, blank=False, null=False)
    enrollment = models.CharField(max_length=40, default='khu')
    image = models.ImageField(blank=True, null=True)
    is_admin = models.BooleanField(default=True, blank=False, null=False)
    email = None
    username = None
    USERNAME_FIELD ='phone'
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.first_name+'['+str(self.enrollment)+']'

    @property
    def get_name(self):
        return self.first_name

    @property
    def getuserid(self):
        return self.id