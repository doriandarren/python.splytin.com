import random
import time
from celery import shared_task
from django.tasks import task
from apps.ai_prompt_generations.services.ai_prompt_generation_service import AiPromptGenerationService
from apps.devs.services.ai_generation_service import AIGenerationService
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

