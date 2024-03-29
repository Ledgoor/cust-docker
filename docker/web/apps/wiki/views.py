import json
from typing import Union
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

from .services import wiki_ws_action
from .wiki_services import get_wiki_categories_menu, _get_page_view_data

from .models import Category, Page

from portal.settings import env

# from apps.search.views import search

def list_pages_view(request):
    """Веб-сервис, отображающий все статьи wiki по категориям"""
    
    wiki_categories_menu = get_wiki_categories_menu()

    return render(request, 'wiki/index.html', {
        'app': mark_safe(json.dumps("wiki")),
        'left_menu': wiki_categories_menu,

        #FIXME
        'VERSION': env('VERSION')
    })

def page_view(request, page_id):
    '''Веб-сервис, показывающий заголовок и содержимое конкретной статьи по id'''

    try:
        data = _get_page_view_data(page_id)
        
        #FIXME
        data['VERSION'] = env('VERSION')

        return render(request, 'wiki/view.html', data)
    except Exception:
        return redirect('/admin/wiki/page/add/')

def wiki(username: str, app: str, message: Union[str, list]) -> str:
    '''
        Веб-сокет - управление приложением Wiki.
        Если переменная message - список, то выполняем нужную фильтрацию.
        Если переменная message - строка, то выполняем поиск.
    '''
    
    result = wiki_ws_action(message)
    return result




def edit_page(request, page_id):
    try:
        page = Page.objects.get(id=page_id)
        content = page.content
    except Page.DoesNotExist:
        content = 'Empty'
    return render(request, 'wiki/edit.html', {
            'app': f'{mark_safe(json.dumps("wiki"))}',
            'page_id': page_id,
            'content:': content
            }
        )

def save_page(request, page_id):
    content = request.POST['content']
    try:
        page = Page.objects.get(id=page_id)
        page.content = content
    except Page.DoesNotExist:
        page = Page(id=page_id, content=content)
    page.save()
    return HttpResponseRedirect('/wiki/' + page_id + '/')