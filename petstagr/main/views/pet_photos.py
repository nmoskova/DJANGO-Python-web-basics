from django.shortcuts import render, redirect

from petstagr.main.forms.pet_photos import CreatePetPhoto, EditPetPhoto, DeletePetPhoto
from petstagr.main.models.pet_model import Pet
from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.views.general import get_profile


def pet_photos_view_action(request, form_class, success_page, template, instance=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_page)

    form = form_class(instance=instance)

    context = {
        'form': form,
        'pet_photo': instance,

    }
    return render(request, template, context)


def photo_details(request, pk):
    pet_photo = PetPhoto.objects.\
        prefetch_related('tagged_pets').\
        get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def add_photo(request):
    return pet_photos_view_action(request, CreatePetPhoto, 'dashboard', 'photo_create.html')


def edit_photo(request, pk):
    return pet_photos_view_action(request, EditPetPhoto, 'dashboard', 'photo_edit.html', PetPhoto.objects.get(pk=pk))


def delete_pet_photo(request, pk):
    return pet_photos_view_action(request, DeletePetPhoto, 'dashboard', 'photo_delete.html', PetPhoto.objects.get(pk=pk))


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo details', pk)