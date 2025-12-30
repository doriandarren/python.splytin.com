from django.db import models


class OllamaText(models.Model):
    model = models.CharField(max_length=100)
    request_prompt = models.CharField(max_length=200, blank=True, null=True)
    request_payload = models.JSONField()
    response_payload = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "singular"
        verbose_name_plural = "plural"
    
    def __str__(self):
        return f"OllamaText: {self.id} - {self.model}"