from rest_framework.serializers import ModelSerializer
from ollama_texts.models import OllamaText


class OllamaTextSerializer(ModelSerializer):
    class Meta:
        model = OllamaText
        fields = "__all__"
        ## fields = ['id']
