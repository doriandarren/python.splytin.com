from rest_framework.serializers import ModelSerializer
from ollama_images.models import OllamaImage


class OllamaImageSerializer(ModelSerializer):
    class Meta:
        model = OllamaImage
        fields = "__all__"
        ## fields = ['id']
