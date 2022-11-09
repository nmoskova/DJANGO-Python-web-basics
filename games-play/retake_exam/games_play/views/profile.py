from django.shortcuts import render

from retake_exam.forms.profile import CreateProfileForm, EditProfileForm, DeleteProfileForm
from retake_exam.games_play.common import get_profile
from retake_exam.games_play.models.game import Game
from retake_exam.games_play.models.profile import Profile
from retake_exam.games_play.common import crud_action


def create_profile(request):
    return crud_action(request, CreateProfileForm, 'show index', Profile(), 'create-profile.html', )


def edit_profile(request):
    return crud_action(request, EditProfileForm, 'details profile', get_profile(), 'edit-profile.html')


def delete_profile(request):
    return crud_action(request, DeleteProfileForm, 'show index', get_profile(), 'delete-profile.html')


def details_profile(request):
    profile = get_profile()
    picture = profile.profile_picture
    games = Game.objects.all()
    games_count = len(games)
    avg_rating = sum(x.rating for x in games)

    context = {
        'profile': profile,
        'picture': picture,
        'games_count': games_count,
        'avg_rating': avg_rating,
    }
    return render(request, 'details-profile.html', context)



