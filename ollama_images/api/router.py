from rest_framework.routers import DefaultRouter

from ollama_images.api.views import OllamaImageApiViewSet

# Add urls.py:
# from ai.api.router import router_ollama
# path('api/v1/', include(router_example.urls))


# example
router_ollama_image = DefaultRouter()

# examples
router_ollama_image.register(
    prefix='ollama_images',
    basename='ollama_images',
    viewset=OllamaImageApiViewSet
)
