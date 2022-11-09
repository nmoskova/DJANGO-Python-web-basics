from django.shortcuts import render

from retake_exam.games_play.common import get_profile
from retake_exam.games_play.models.game import Game


def show_index(request):
    context = {
        'profile': get_profile(),
    }
    return render(request, 'home-page.html', context)


def show_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)
