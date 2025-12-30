from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ollama_images.api.serializers import OllamaImageSerializer
from ollama_images.models import OllamaImage


class OllamaImageApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OllamaImageSerializer
    queryset = OllamaImage.objects.all()
