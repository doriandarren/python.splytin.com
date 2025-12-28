from django.contrib import admin
from ai.models import Ollama

@admin.register(Ollama)
class OllamaAdmin(admin.ModelAdmin):
    pass
