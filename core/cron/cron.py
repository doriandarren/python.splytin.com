# core/cron.py
from django.utils import timezone

from core.messages.message_channel import MessageChannel

def hello_cron():
    
    MessageChannel.send("hello cron")
    
    print(f"[CRON] hello_cron ejecutado: {timezone.now()}")