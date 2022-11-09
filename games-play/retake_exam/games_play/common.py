from django.shortcuts import redirect, render

from retake_exam.games_play.models.game import Game
from retake_exam.games_play.models.profile import Profile


def get_profile():
    return Profile.objects.first()


def get_game(pk):
    return Game.objects.get(pk=pk)


def crud_action(request, form_class, success_page, instance, template, ctx={}):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_page)

    form = form_class(instance=instance)
    context = {
        'form': form
    }
    context.update(ctx)

    return render(request, template, context)