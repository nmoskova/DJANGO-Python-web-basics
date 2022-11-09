from django import forms
from django.forms import PasswordInput

from retake_exam.games_play.models.game import Game
from retake_exam.games_play.models.profile import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password',)
        widgets = {
            "password": PasswordInput(
                attrs={
                    'placeholder':'********',
                     'autocomplete': 'off',
                     'data-toggle': 'password'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
