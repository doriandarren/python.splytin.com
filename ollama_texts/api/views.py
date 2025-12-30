from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ollama_texts.api.serializers import OllamaTextSerializer
from ollama_texts.models import OllamaText


class OllamaTextApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = OllamaTextSerializer
    queryset = OllamaText.objects.all()
