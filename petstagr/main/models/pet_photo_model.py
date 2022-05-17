from django.db import models

from petstagr.main.common.validators import ValidatePhotoMaxSizeMB
from petstagr.main.models.pet_model import Pet


class PetPhoto(models.Model):
    """
    Pet's Photo
    The user must provide the following information when uploading a pet's photo in their profile:
    •	Photo - the maximum size of the photo can be 5MB
    •	Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
    The user may provide the following information when uploading a pet's photo in their profile:
    •	Description - a user can write any description about the picture, with no limit of words/chars
    Other:
    •	Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
    •	Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited.
    """

    PHOTO_MAX_SIZE_MB = 5

    LIKES_DEFAULT = 0

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=(ValidatePhotoMaxSizeMB(PHOTO_MAX_SIZE_MB),)
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=LIKES_DEFAULT,
    )



