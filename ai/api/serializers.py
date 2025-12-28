from rest_framework.serializers import ModelSerializer
from ai.models import Ollama


class OllamaSerializer(ModelSerializer):
    class Meta:
        model = Ollama()
        fields = ['id']
