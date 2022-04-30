from cgitb import reset
from nis import cat
from unicodedata import category
from importlib.metadata import PackageNotFoundError
from importlib.resources import contents
import json
from unittest import result
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.shortcuts import redirect

from apps.wiki.models import Category, Page

# from apps.search.views import search

def index(request):
    """Рендерит страницу со списком страниц wiki"""
    

    def gen_left_menu():
        pages = Page.objects.all()
        categories = Category.objects.all()

        result = ''
        for category in categories:
            pages_by_category_count = pages.filter(category=category.id).count()
            action = "searchSocket.send(JSON.stringify({'message': ['filter_category', '" + str(category.id) + "']}));"
            result += f'<a type="submit" onclick="{action}">{category.name} ({pages_by_category_count})</a><br>'
        return result
    left_menu = gen_left_menu()

    return render(request, 'wiki/index.html', {
        'app': f'{mark_safe(json.dumps("wiki"))}',
        'left_menu': left_menu,
    })

def view_page(request, page_id):
    try:
        page = Page.objects.get(id=page_id)
        content = page.content
        page_name = page.name
        return render(request, 'wiki/view.html', {
                'app': f'{mark_safe(json.dumps("wiki"))}',
                'page': page,
                'page_id': page_id,
                'page_name': page_name,
                'content': content
                }
            )
    except Exception:
        return redirect('/admin/wiki/page/add/')

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



def wiki(username, app, message):
    '''
        Управляем полученнными сообщениями
        Если список то выполняем нужную фильтрацию
        Если строка, то выполняем поиск
    '''
    
    print('message', type(message), message)
        
    if isinstance(message, list) is True:
        if message[0] == 'filter_category':
            if message[1] != 'clear':
                category_id = message[1]
                return get_pages_by_category(category_id)
            else:
                return get_all_pages_sorted_by_categories()
    else:
        #иначе это что то ввели в строку поиска
        result = search(username, app, message)

    return result


def get_pages_by_category(category_id):
    category_name = Category.objects.get(id=category_id).name
    pages = Page.objects.filter(category=category_id)
    result = f'<h2>{category_name}</h2>'
    if len(pages) == 0:
        result += 'В этой категории нет записей.<hr>'
    else:
        for page in pages:
            result += f'<a href="/wiki/{page.id}">{page.name}</a><br>'
        result += '<hr>'
    return result

def get_all_pages_sorted_by_categories():
    '''
        Выводит страницы конкретной категории.
        На входе id катергрии (int).
        На выходе HTML-код со всеми записями в категории.
    '''
    categories = Category.objects.all()
    result = ''
    for category in categories:
        pages = Page.objects.filter(category=category.id)
        
        result += f'<h2>{category.name}</h2>'
        if len(pages) == 0:
            result += f'В этой категории нет записей.<hr>'
        else:
            for page in pages:
                result += f'<a href="/wiki/{page.id}">{page.name}</a><br>'
            result += '<hr>'
    return result