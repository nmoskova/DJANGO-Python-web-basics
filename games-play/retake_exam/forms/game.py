from django import forms

from retake_exam.games_play.models.game import Game


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'
