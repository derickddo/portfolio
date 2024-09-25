from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(blank=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True, upload_to='resumes/', help_text='Upload your resume here.', verbose_name='Resume')
    link_to_resume = models.URLField(blank=True, null=True, help_text='Provide a link to your resume.', verbose_name='Link to Resume')

    @receiver(signal=post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)


    @receiver(signal=post_save, sender=User)
    def update_profile(sender, instance, created, **kwargs):
        if created == False:
            instance.userprofile.save()
    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username

class Technology(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField()

    class Meta:
        db_table = 'technology'
        verbose_name_plural = 'technologies'
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField(blank=True)
    technologies_used = models.ManyToManyField(Technology)
    project_image = models.ImageField(help_text='Upload a picture of your project here.', verbose_name='Project Image', blank=True, null=True)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.title

class IssuingOrganization(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(help_text='Upload a picture of the organization\'s logo here.', verbose_name='Organization Logo', blank=True, null=True)

    class Meta:
        db_table = 'issuing_organization'

    def __str__(self):
        return self.name
    
class Certification(models.Model):
    title = models.CharField(max_length=30)
    issuing_organization = models.ForeignKey(IssuingOrganization, on_delete=models.CASCADE)
    date_received = models.DateField()
    image = models.ImageField(help_text='Upload a picture of your certificate here.', verbose_name='Certificate Image', blank=True, null=True)

    class Meta:
        db_table = 'certification'

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        db_table = 'contact'

    def __str__(self):
        return self.name