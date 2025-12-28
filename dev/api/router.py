from rest_framework.routers import DefaultRouter
from dev.api.views import DevApiViewSet

# Add urls.py:
# from ai.api.router import router_ollama
# path('api/v1/', include(router_example.urls))


# example
router_dev = DefaultRouter()

# examples
router_dev.register(
    prefix='dev',
    basename='dev',
    viewset=DevApiViewSet
)
