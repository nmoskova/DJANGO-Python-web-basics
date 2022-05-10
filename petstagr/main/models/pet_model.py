import datetime

from django.db import models

from petstagr.main.models.profile_model import Profile


class Pet(models.Model):
    """
            Pet
        The user must provide the following information when adding a pet in their profile:
        •	Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
        •	Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
        The user may provide the following information when adding a pet to their profile:
        •	Date of birth - pet's day, month, and year of birth.
    """

    NAME_MAX_LEN = 30
    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"
    ANIMALS = (CAT, DOG, BUNNY, PARROT, FISH, OTHER)
    ANIMALS_CHOICES = [(x, x) for x in ANIMALS]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    type = models.CharField(
        max_length=max(len(x) for (_, x) in ANIMALS_CHOICES),
        choices=ANIMALS_CHOICES,
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    @property
    def age(self):
        years = datetime.datetime.now().year - self.date_of_birth.year
        return years

    class Meta:
        unique_together = ('user', 'name')