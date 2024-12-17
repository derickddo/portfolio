from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile, Project, Certification, Contact
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from core.settings import EMAIL_HOST_USER

# import messages
from django.contrib import messages

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

class ContactView(View):

    def get(self, request: HttpRequest):
        return render(request, 'portfolio/contact.html')
    
    def post(self, request: HttpRequest):
        email = request.POST['email']
        message = request.POST['message']
        print(email, message)
    
        # send email
        try:
            email = EmailMessage(
                subject='New Contact Form Submission',
                body=f'Email: {email}\nMessage: {message}',
                from_email=email,
                to=[EMAIL_HOST_USER],
            )
            
            email.send()
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            print(str(e))
            messages.error(request, f'There was an error sending your message.{str(e)}')
        return redirect('home')
        

class CertificationListView(ListView):
    model = Certification
    template_name = 'portfolio/certifications.html'
    context_object_name = 'certifications'

    def get_queryset(self):
        return Certification.objects.order_by('-date_received').all()

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
        
   