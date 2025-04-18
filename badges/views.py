from django.shortcuts import render
from django.conf import settings
from django.contrib.staticfiles.views import serve

def badge_list(request):
    return render(request, 'index.html')

def badge_detail(request, badge_id):
    context = {
        'badge_id': badge_id
    }
    return render(request, 'index.html', context)

def serve_static(request, path):
    if settings.DEBUG:
        return serve(request, path)
