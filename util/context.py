# Create your views here.
import settings

def add_settings(request):
    '''Add some settings to the cotext'''

    return {
        'SITE_URL': settings.SITE_URL,
    }
