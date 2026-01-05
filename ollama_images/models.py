from django.db import models


class OllamaImage(models.Model):
    # fields
    
    ollama_text_id = models.ForeignKey('ollama_texts.OllamaText', on_delete=models.CASCADE)
    request_prompt = models.CharField(max_length=200, blank=True, null=True)
    request_payload = models.JSONField()
    response_payload = models.JSONField(blank=True, null=True)
    nonce = models.CharField(max_length=100)
    sampler_index = models.CharField(max_length=200)
    cfg_scale = models.FloatField()
    seed = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    steps = models.IntegerField()
    image_bytes = models.BinaryField(null=True, blank=True)
    image_mime = models.CharField(max_length=50, default="image/png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "singular"
        verbose_name_plural = "plural"
    
    def __str__(self):
        return f"OllamaImage: {self.id} - {self.model}"