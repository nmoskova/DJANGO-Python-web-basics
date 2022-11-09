from django.shortcuts import render

from retake_exam.forms.game import CreateGameForm, EditGameForm, DeleteGameForm
from retake_exam.games_play.common import get_profile, get_game
from retake_exam.games_play.models.game import Game
from retake_exam.games_play.common import crud_action


def create_game(request):
    ctx = {
        'profile': get_profile()
    }
    return crud_action(request, CreateGameForm, 'show dashboard', Game(), 'create-game.html', ctx)


def edit_game(request, pk):
    game = get_game(pk)

    ctx = {
        'profile': get_profile(),
        'game': game,
    }
    return crud_action(request, EditGameForm, 'show dashboard', game, 'edit-game.html', ctx)


def delete_game(request, pk):
    game = get_game(pk)

    ctx = {
        'profile': get_profile(),
        'game': game,
    }
    return crud_action(request, DeleteGameForm, 'show dashboard', game, 'delete-game.html', ctx)


def details_game(request, pk):
    profile = get_profile()
    game = get_game(pk)

    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'details-game.html', context)





