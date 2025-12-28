from rest_framework.routers import DefaultRouter
from ai.api.views import OllamaApiViewSet

router_ollama = DefaultRouter()

router_ollama.register(
    prefix='ollama',
    basename='ollama',
    viewset=OllamaApiViewSet
)
