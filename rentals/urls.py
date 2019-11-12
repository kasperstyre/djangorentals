from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rentals', views.rental_list),
    path('rentals/<int:pk>', views.rental_detail)
]