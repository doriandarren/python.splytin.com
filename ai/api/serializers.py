from rest_framework.serializers import ModelSerializer
from ai.models import Ollama


class OllamaSerializer(ModelSerializer):
    class Meta:
        model = Ollama
        #fields = ['model', 'request_prompt','request_payload', 'response_payload', 'created_at', 'updated_at']
        fields = "__all__"
