from django.shortcuts import render

from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.models.profile_model import Profile


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def show_index(request):
    hide_items_from_nav_bar = True

    context = {
        'hide_nav_bar': hide_items_from_nav_bar,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user=profile).distinct()
    context = {
       'pet_photos': pet_photos,
    }
    return render(request, 'dashboard.html', context)