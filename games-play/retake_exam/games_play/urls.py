from django.urls import path

from retake_exam.games_play.views.profile import create_profile, details_profile, edit_profile, delete_profile
from retake_exam.games_play.views.generic import show_index, show_dashboard
from retake_exam.games_play.views.game import create_game, details_game, edit_game, delete_game

urlpatterns = [
    path('', show_index, name='show index'),
    path('dashboard/', show_dashboard, name='show dashboard'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', details_game, name='details game'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),

    path('profile/create/',  create_profile, name ='create profile'),
    path('profile/details/',  details_profile, name='details profile'),
    path('profile/edit/',  edit_profile, name='edit profile'),
    path('profile/delete/',  delete_profile, name='delete profile'),
]