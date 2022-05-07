from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    only_letters_validation_message_raise = 'Value should consist only of letters'
    if not value.isalpha():
        raise ValidationError(only_letters_validation_message_raise)


@deconstructible
class ValidatePhotoMaxSizeMB:
    def __init__(self, image_max_size_mb):
        self.image_max_size_mb = image_max_size_mb

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes():
            raise ValidationError(self.__get_exception_message)

    def __megabytes_to_bytes(self):
        return self.image_max_size_mb * 1024 * 1024

    def __get_exception_message(self):
        return f" The maximum size of the photo can be {self.image_max_size_mb:.2f}MB"

