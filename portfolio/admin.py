from django.contrib import admin
from .models import UserProfile, Technology, Project, Certification, Contact

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Contact)
