from cgitb import reset
from email import message
import json
from unittest import result

from django.shortcuts import render
from django.utils.safestring import mark_safe

from apps.chat.views import chat
from apps.wiki.views import wiki

def websocket(app, username, message):
    '''
    Маршрутизируем входящее сообщение в нужное приложение
    Тут только дефолтные, остальноые в consumers в каждом приложении
    '''

    # if app == 'search':
    #     result = search(username, app, message)
    if app == 'chat':
        result = chat(message)
    elif app == 'wiki':
        result = wiki(username, app, message)
    else:
        return f'Приложение: {app}, Сообщение: {message} - нет инструкций!'
    return result