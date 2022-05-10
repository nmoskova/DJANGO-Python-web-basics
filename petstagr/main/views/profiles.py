from django.shortcuts import render, redirect

from petstagr.main.forms.profile import CreateProfileForm, EditProfileForm, DeleteProfileForm
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


def crud_view(request, form, success_page, template, instance=None):
    if request.method == 'POST':
        form = form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_page)

    form = form(instance=instance)

    context = {
        'form': form,
    }
    return render(request, template, context)


def create_profile(request):
    return crud_view(request, CreateProfileForm, 'index', 'profile_create.html')


def edit_profile(request):
    return crud_view(request, EditProfileForm, 'show profile', 'profile_edit.html', get_profile())


def delete_profile(request):
    return crud_view(request, DeleteProfileForm, 'index', 'profile_delete.html', get_profile())




