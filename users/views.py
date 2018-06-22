from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from users.models import Users
from users.serializer import UserSerializer, AuthSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()


class AuthUser(APIView):
    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = UserSerializer(instance=serializer.validated_data['user']).data
        return Response(response)
