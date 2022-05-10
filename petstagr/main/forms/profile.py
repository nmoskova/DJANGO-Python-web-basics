from django import forms

from petstagr.main.helpers import BootstrapFormMixin
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

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
            'date_of_birth': forms.DateInput(
                attrs={
                    'min': '1920-01-01',
                }
            ),
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
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

