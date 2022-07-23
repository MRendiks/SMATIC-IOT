import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from .role_model import Role


class UserManager(BaseUserManager):

    def create_logistic_owner(
            self,
            name: str,
            email: str,
            password: str,
            phone: str,
            address: str,
            role_id: int = Role.LOGISTIC_OWNER_ID
    ):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.phone = phone
        user.address = address
        user.role = Role.objects.get(id=role_id)
        user.save()

        return user

    def create_warehouse_employee(
            self,
            name: str,
            email: str,
            password: str,
            phone: str,
            address: str,
            role_id: int = Role.WAREHOUSE_EMPLOYEE_ID
    ):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.phone = phone
        user.address = address
        user.role = Role.objects.get(id=role_id)
        user.save()

        return user

    def create_warehouse_owner(
            self,
            name: str,
            email: str,
            password: str,
            phone: str,
            address: str,
            role_id: int = Role.WAREHOUSE_OWNER_ID
    ):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.name = name
        user.phone = phone
        user.address = address
        user.role = Role.objects.get(id=role_id)
        user.save()

        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, null=False)
    email = models.EmailField(unique=False, max_length=64, null=False)
    password = models.CharField(max_length=128, null=False)
    address = models.TextField(null=False)
    phone = models.CharField(unique=False, max_length=24, null=False)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    objects = UserManager()

    USERNAME_FIELD = 'id'

    class Meta:
        app_label = 'user'
        db_table = 'user'
