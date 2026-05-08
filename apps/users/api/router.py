from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserApiViewSet, UserView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




# Add urls.py:
# from apps.users.api.router import router_user
# path('api/v1/', include(router_user.urls))


# example
router_user = DefaultRouter()

# examples
router_user.register(
    prefix='users',
    basename='users',
    viewset=UserApiViewSet
)


urlpatterns = [
    path('auth/me/', UserView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]