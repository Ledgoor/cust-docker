import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
from portal.settings import env


def home_view(request):
    """Веб-сервис, отображающий главную страницу проекта"""
    

    return render(request, 'home/index.html', {
        'app': mark_safe(json.dumps("home")),

        #FIXME
        'VERSION': env('VERSION')
    })