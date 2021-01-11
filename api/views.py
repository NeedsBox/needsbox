from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from rest_framework.viewsets import GenericViewSet

from accounts.models import Account
from project.models import Advertisement
from api.serializers import UserSerializer, AdvertisementSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET'])
def adList(request):
    posts = Advertisement.objects.all()
    
    serializer = AdvertisementSerializer(posts, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def userList(request):
    users = Account.objects.all()
    
    serializer = UserSerializer(users, many=True)
    
    return Response(serializer.data)
