# Create your views here.
from rest_framework import status, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response

from accounts.models import Account
from api.serializers import UserSerializer


@api_view(['GET'])
def verify_token(request, token: str):
    result = status.HTTP_404_NOT_FOUND
    if Token.objects.filter(key=token).exists():
        result = status.HTTP_200_OK

    return Response(status=result)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def perform_update(self, serializer: UserSerializer):
        user: Account = self.request.user
        is_admin = bool(user and user.is_staff)
        username = serializer.data["username"]
        if (not is_admin) and username != user.username:
            exception = APIException("User is not allowed to modify other users")
            exception.status_code = status.HTTP_401_UNAUTHORIZED
            raise exception
        super().perform_update(serializer)