from django.urls import path
from .views import HomeView, ProjectListView, ProjectDetailView, ContactView

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('projects/', ProjectListView.as_view(), name='projects'),
     path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
     path('contact/', ContactView.as_view(), name='contact'),
]