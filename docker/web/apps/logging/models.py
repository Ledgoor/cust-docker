from sqlite3 import Timestamp
from django.db import models

class WS(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    timestamp = models.DateTimeField(u'Время события')
    username = models.CharField(max_length=20)
    app = models.CharField(max_length=20)
    message = models.CharField(max_length=500)