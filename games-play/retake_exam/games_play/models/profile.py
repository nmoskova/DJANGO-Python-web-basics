from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
