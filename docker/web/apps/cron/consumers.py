from channels.consumer import SyncConsumer
# from lib.telegram import tg_send_message, chat_availability
from datetime import datetime
# from lib.jira import get_new_tt_mrg1

###########################################
# https://github.com/rajasimon/beatserver #
###########################################

# Для запуска - python manage.py beatserver

class PrintConsumer(SyncConsumer):
    def test_print(self, message):
        print(message)

# class JiraUpdateConsumer(SyncConsumer):
#     def jira_get_tt(self, message):
#         get_new_tt_mrg1()

# class AvailabilityConsumer(SyncConsumer):
#     def index(self, message):
#         tg_send_message(f'ping - {datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}', id=chat_availability)