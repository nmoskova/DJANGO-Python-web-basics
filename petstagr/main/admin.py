from django.contrib import admin
from django.contrib.admin import StackedInline

from petstagr.main.models.pet_model import Pet
from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.models.profile_model import Profile


class PetInlineAdmin(StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name',)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
