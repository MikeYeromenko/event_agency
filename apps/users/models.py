import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.common.utils import check_password, make_password
from apps.users.managers import UserManager


class User(BaseModel, AbstractBaseUser):
    """
    Django user model
    """

    class RolesChoices:
        ADMIN = 1
        MANAGER = 2
        CLIENT = 3

        CHOICES = ((ADMIN, _("Admin")),)
        DEFAULT = CLIENT

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    email = models.EmailField(_("Email"), max_length=50, unique=True)
    first_name = models.CharField(_("first name"), max_length=30, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    role = models.PositiveSmallIntegerField(_("Role"), choices=RolesChoices.CHOICES, default=RolesChoices.DEFAULT)

    objects = UserManager()

    class Meta:
        verbose_name_plural = "Users"
        ordering = ("email",)
        db_table = "user"

    @classmethod
    def get_user(cls, user_id: uuid.UUID): ...

    def set_password(self, raw_password: str) -> None:
        make_password(...)
        ...

    def check_password(self, raw_password: str) -> bool:
        check_password(password=raw_password)
        ...

    def change_password(self, new_password: str) -> None: ...
