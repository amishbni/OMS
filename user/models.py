from django.contrib.auth.models import AbstractUser
from django.db import models

from enum import IntEnum
from typing import Tuple

from core.models import BaseModel


class Role(IntEnum):
    ADMIN = 0
    CUSTOMER = 1


class User(AbstractUser, BaseModel):
    ROLES: Tuple[tuple] = (
        (Role.ADMIN.value, "Administrator"),
        (Role.CUSTOMER.value, "Customer"),
    )

    role = models.SmallIntegerField(choices=ROLES, default=Role.CUSTOMER.value)

    @property
    def is_admin(self) -> bool:
        return self.role == Role.ADMIN.value

    @property
    def is_customer(self) -> bool:
        return self.role == Role.CUSTOMER.value
