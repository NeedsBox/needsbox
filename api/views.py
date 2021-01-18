# Create your views here.
from rest_framework import status, permissions, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin

from accounts.models import Account
from api.serializers import UserSerializer, CategorySerializer, AdvertisementSerializer, ServiceSerializer, \
    ReviewSerializer
from project.models import Category, Advertisement, Service, Review


@api_view(['GET'])
def verify_token(request, token: str):
    result = status.HTTP_404_NOT_FOUND
    if Token.objects.filter(key=token).exists():
        result = status.HTTP_200_OK

    return Response(status=result)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class AdListView(ListAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'location__district', 'location__city', 'category__name', 'description')


class ServiceListView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'location__district', 'location__city', 'category__name', 'description')


class CustomModelViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super().get_permissions()

    def perform_update(self, serializer: UserSerializer):
        user: Account = self.request.user
        is_admin = bool(user and user.is_staff)
        username = serializer.data["user"]["username"]
        if (not is_admin) and username != user.username:
            exception = APIException("User is not allowed to modify other users objects")
            exception.status_code = status.HTTP_401_UNAUTHORIZED
            raise exception
        super().perform_update(serializer)


class ReviewViewSet(NestedViewSetMixin, CustomModelViewSet, mixins.ListModelMixin):
    """
    API endpoint that allows ads to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


class AdViewSet(CustomModelViewSet):
    """
    API endpoint that allows ads to be viewed or edited.
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    lookup_field = 'id'


class ServiceViewSet(CustomModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'


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
