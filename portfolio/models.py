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
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.URLField(blank=True)
    technologies_used = models.ManyToManyField(Technology)

    class Meta:
        db_table = 'project'

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    title = models.CharField(max_length=30)
    issuing_organization = models.CharField(max_length=50)
    date_received = models.DateField()

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