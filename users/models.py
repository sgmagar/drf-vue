from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

import os
import uuid


def get_profile_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "{}.{}".format(uuid.uuid4(), ext)[:99]
    return os.path.join('uploads/profile-pics/', filename)


class UserManager(BaseUserManager):
    def create_user(self, full_name='', password=None, email=None, active=True):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(
            full_name=full_name,
            email=email,
        )
        if password:
            user.set_password(password)
        user.is_active = active
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name='', password=None, email=None,):
        user = self.create_user(
            full_name=full_name,
            password=password,
            email=email
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=245)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    profile_picture = models.ImageField(upload_to=get_profile_picture_path, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def data(self):
        from .api.serializers import UserSerializer
        return UserSerializer(self).data

    def __str__(self):
        return self.full_name

