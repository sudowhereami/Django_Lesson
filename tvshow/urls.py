from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.tvshow, name='tvshow'),
    path('shows/<int:id>/', views.tvshow_detail, name='detail'),
    path('shows/<int:id>/update/', views.show_update, name='update'),
    path('shows/<int:id>/delete/', views.show_delete, name='delete'),
    path('add-shows/', views.add_shows, name='addtvshow')
]
