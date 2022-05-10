from django.shortcuts import render, redirect

from petstagr.main.models.pet_photo_model import PetPhoto


def photo_details(request, pk):
    pet_photo = PetPhoto.objects.\
        prefetch_related('tagged_pets').\
        get(pk=pk)
    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def add_photo(request):
    return render(request, 'photo_create.html')


def edit_photo(request, pk):
    return render(request, 'photo_edit.html')


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()
    return redirect('photo details', pk)