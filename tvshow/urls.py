from django.urls import path
from . import views

urlpatterns = [
    path('shows/', views.TVShowView.as_view(), name='tvshow'),
    path('shows/<int:id>/', views.TVShowDetailView.as_view(), name='detail'),
    path('shows/<int:id>/update/', views.TVShowUpdateView.as_view(), name='update'),
    path('shows/<int:id>/delete/', views.TVShowDeleteView.as_view(), name='delete'),
    path('add-shows/', views.TVShowCreateView.as_view(), name='addtvshow')
]
