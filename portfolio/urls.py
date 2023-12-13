from django.urls import path
from .views import HomeView, ProjectListView, ProjectDetailView, ContactView, CertificationListView, AboutView

urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('projects/', ProjectListView.as_view(), name='projects'),
     path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
     path('contact/', ContactView.as_view(), name='contact'),
     path('certifications/', CertificationListView.as_view(), name='certifications'),
     path('about/', AboutView.as_view(), name='about'),
]