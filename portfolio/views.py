from django.shortcuts import render, redirect
from .models import UserProfile, Technology, Project, Certification, Contact
from django.views.generic import TemplateView, ListView, DetailView, CreateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = UserProfile.objects.first()
        return context

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

class CertificationListView(ListView):
    model = Certification
    template_name = 'portfolio/certifications.html'
    context_object_name = 'certifications'

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
        
   