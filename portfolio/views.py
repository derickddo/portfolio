from django.shortcuts import render, redirect
from .models import UserProfile, Technology, Project, Certification, Contact
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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

class CertificationListView(ListView):
    model = Certification
    template_name = 'portfolio/certifications.html'
    context_object_name = 'certifications'

@method_decorator(csrf_exempt, name='dispatch')
class StateView(View):
    counter = 0
    def get(self, request, *args, **kwargs):
        return JsonResponse({'counter': self.counter})

    def post(self, request, *args, **kwargs):
        self.counter += 1
        return HttpResponse(str(self.counter))
        
   