from django.shortcuts import render

from petstagr.main.models.pet_model import Pet
from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.views.general import get_profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user=profile)
    pet_photos = PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets=pets).distinct()
    total_images = len(pet_photos)
    total_likes = sum(pp.likes for pp in pet_photos)

    context = {
        'profile': profile,
        'pets': pets,
        'total_images': total_images,
        'total_likes': total_likes,
    }
    return render(request, 'profile_details.html', context)
