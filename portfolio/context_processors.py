from .models import UserProfile

def get_global_context(request):
    return {
        'profile': UserProfile.objects.first(),
    }