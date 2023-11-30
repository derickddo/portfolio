from django.shortcuts import render
from .models import UserProfile, Technology, Project, Certification, Contact
from django.views.generic import TemplateView, ListView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'