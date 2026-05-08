from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend


from apps.users.api.serializers import UserSerializer
from apps.users.models import User


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # Filtros...
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'active']





class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serialize = UserSerializer(request.user)
        return Response(serialize.data)