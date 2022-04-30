from apps.websocket.consumers import GlobalConsumer

from asgiref.sync import async_to_sync
from datetime import datetime

from .views import get_all_pages_sorted_by_categories

class WikiConsumer(GlobalConsumer):
    
    def connect_message(self):
        '''При подключении подгружаем все статьи отсортированные по категориям'''

        content = get_all_pages_sorted_by_categories()
        async_to_sync(self.channel_layer.group_send)(
            self.group,
            {
                'type': 'message_send',
                'message': content
            }
        )