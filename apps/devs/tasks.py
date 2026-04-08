import time
from celery import shared_task
from core.messages.message_channel import MessageChannel


@shared_task
def start():
    try: 

        MessageChannel.send(
            text=f"invoke ejecutado: {time.time()} | ai_text_generation_id={time.time()}",
            title="CRON TASKS",
        )

    except Exception as e:
        MessageChannel.send(
            text=f"error: {str(e)}",
            title="CRON ERROR TEXT GENERATION",
            is_error=True
        )
    return "ok"

