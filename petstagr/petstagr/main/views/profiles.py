from django.shortcuts import render, redirect

from petstagr.main.forms.profile import ProfileForm
from petstagr.main.models.pet_model import Pet
from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.views.general import get_profile


def show_profile(request):
    profile = get_profile()
    pets = Pet.objects.filter(user=profile)
    pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()
    total_images = len(pet_photos)
    total_likes = sum(pp.likes for pp in pet_photos)

    context = {
        'profile': profile,
        'pets': pets,
        'total_images': total_images,
        'total_likes': total_likes,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile_create.html', context)


def edit_profile(request):

    return render(request, 'profile_edit.html')


def delete_profile(request):
    return render(request, 'profile_delete.html')

