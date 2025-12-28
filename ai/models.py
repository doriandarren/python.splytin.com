from django.db import models


class Ollama(models.Model):
    model = models.CharField(max_length=100)
    request_payload = models.JSONField()
    response_payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "ollama"
        verbose_name_plural = "ollamas"
    
    def __str__(self):
        return f"Ollama: {self.id} - {self.model}"
