from .models import WS
from datetime import datetime

def log(username, app, message):    
    timestamp = datetime.now()
    WS.objects.create(username=username, timestamp=timestamp, message=message, app=app)
    return