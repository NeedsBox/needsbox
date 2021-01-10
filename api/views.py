from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from accounts.models import Account
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]