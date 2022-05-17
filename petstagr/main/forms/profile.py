import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date

from petstagr.main.helpers import BootstrapFormMixin
from petstagr.main.models.pet_photo_model import PetPhoto
from petstagr.main.models.profile_model import Profile


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        labels = {
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter first name',
            },
        ),
            'last_name': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter last name',
            },
        ),
            'picture': forms.TextInput(
                attrs={
                    # 'class': 'form-control',
                    'placeholder': 'Enter URL',
            },
        )
    }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or \
                date_of_birth > self.MAX_DATE_OF_BIRTH:
            raise ValidationError(f"Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}")
        return date_of_birth

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'date_of_birth', 'email', 'gender', 'description')
        labels = {
            'picture': 'Link to Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                },
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                },
            ),
            'date_of_birth': forms.DateField(),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter Email',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                }
            ),

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

