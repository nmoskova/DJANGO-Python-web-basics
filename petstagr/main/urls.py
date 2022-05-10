from django.urls import path

from petstagr.main.views.general import show_index, show_dashboard
from petstagr.main.views.pet_photos import photo_details, like_pet_photo, add_photo, edit_photo
from petstagr.main.views.pets import add_pet, edit_pet, delete_pet
from petstagr.main.views.profiles import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('pet/add/', add_pet, name='add pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),

    path('photo/details/<int:pk>/', photo_details, name='photo details'),
    path('photo/add/', add_photo, name='add photo'),
    path('photo/edit/<int:pk>/', edit_photo, name='edit photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

)
