from django.shortcuts import render, redirect

from petstagr.main.forms.pets import CreatePetForm, EditPetForm, DeletePetForm
from petstagr.main.models.pet_model import Pet
from petstagr.main.views.general import get_profile


def pet_view_action(request, form_class, success_page, template, instance=None):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_page)

    form = form_class(instance=instance)

    context = {
        'form': form,
        'pet': instance,

    }
    return render(request, template, context)


def add_pet(request):
    return pet_view_action(request, CreatePetForm, 'show profile', 'pet_create.html', Pet(user=get_profile()))


def edit_pet(request, pk):
    return pet_view_action(request, EditPetForm, 'show profile', 'pet_edit.html', Pet.objects.get(pk=pk))


def delete_pet(request, pk):
    return pet_view_action(request, DeletePetForm, 'show profile', 'pet_delete.html', Pet.objects.get(pk=pk))

