from django.db import models


class Token(models.Model):
    """
    The authorization token model.
    """

    ...

    class Meta:
        db_table = "token"

    def __str__(self):
        return ...
