# Generated by Django 5.0.6 on 2024-06-03 13:11

import uuid

from django.db import migrations, models

import apps.users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="UUID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "email",
                    models.EmailField(max_length=50, unique=True, verbose_name="Email"),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=30, null=True, verbose_name="first name"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, null=True, verbose_name="last name"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text=(
                            "Designates whether this user should be treated as active. Unselect this instead"
                            " of deleting accounts."
                        ),
                        verbose_name="active",
                    ),
                ),
                (
                    "role",
                    models.PositiveSmallIntegerField(choices=[(1, "Admin")], default=3, verbose_name="Role"),
                ),
            ],
            options={
                "verbose_name_plural": "Users",
                "db_table": "user",
                "ordering": ("email",),
            },
            managers=[
                ("objects", apps.users.managers.UserManager()),
            ],
        ),
    ]