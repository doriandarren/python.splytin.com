from rest_framework.routers import DefaultRouter

from ollama_texts.api.views import OllamaTextApiViewSet

# Add urls.py:
# from ai.api.router import router_ollama
# path('api/v1/', include(router_example.urls))


# example
router_text = DefaultRouter()

# examples
router_text.register(
    prefix='ollama_texts',
    basename='ollama_texts',
    viewset=OllamaTextApiViewSet
)
