from django.urls import path

from petstagr.main.views.general import show_index, show_dashboard
from petstagr.main.views.pet_photos import photo_details, like_pet_photo
from petstagr.main.views.profiles import show_profile

urlpatterns = (
    path('', show_index, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),

    path('profile/', show_profile, name='profile'),

    path('photo/details/<int:pk>/', photo_details, name='photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo')
)
