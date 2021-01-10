from rest_framework import serializers

from accounts.models import Account


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'name', 'biography', 'contact', 'website', 'account_type']
