from django.shortcuts import render
from .models import UserProfile, Technology, Project, Certification, Contact
from django.views.generic import TemplateView, ListView, DetailView, CreateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    template_name = 'portfolio/project_detail.html'
    
    def get_object(self):
        return Project.objects.get(pk=self.kwargs['pk'])

class ContactView(CreateView):
    template_name = 'portfolio/contact.html'
    model = Contact
    fields = '__all__'
