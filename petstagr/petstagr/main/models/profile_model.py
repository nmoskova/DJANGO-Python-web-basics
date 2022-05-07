from django.core.validators import MinLengthValidator
from django.db import models

from petstagr.main.common.validators import validate_only_letters


class Profile(models.Model):
    """
    Profile
    The user must provide the following information in their profile:
    •	The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
    •	The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
    •	Profile picture - the user can link their picture using a URL.

    The user may provide the following information in their profile:
    •	Date of birth: day, month, and year of birth.
    •	Description - a user can write any description about themselves, no limit of words/chars.
    •	Email - a user can only write a valid email address.
    •	Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
    """

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30

    MALE = "Male"
    FEMALE = "Female"
    DO_NOT_SHOW = "Do not show"
    GENDERS = (MALE, FEMALE, DO_NOT_SHOW)
    GENDER_CHOICES = [(x, x) for x in GENDERS]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for (_, x) in GENDER_CHOICES),
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'