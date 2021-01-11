# Create your views here.
import uuid

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def verify_token(request, token: str):
    result = status.HTTP_404_NOT_FOUND
    if Token.objects.filter(key=token).exists():
        result = status.HTTP_200_OK

    return Response(status=result)

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Account.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# @api_view(['GET'])
# def adList(request):
#     posts = Advertisement.objects.all()
#
#     serializer = AdvertisementSerializer(posts, many=True)
#
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def userList(request):
#     users = Account.objects.all()
#
#     serializer = UserSerializer(users, many=True)
#
#     return Response(serializer.data)
