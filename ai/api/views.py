from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ai.api.serializers import OllamaSerializer
from ai.models import Ollama


class OllamaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OllamaSerializer()
    queryset = Ollama.objects.all()

