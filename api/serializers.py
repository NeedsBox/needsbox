from rest_framework import serializers

from accounts.models import Account
from project.models import Advertisement, Category, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'name', 'biography', 'contact', 'website', 'account_type']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'district',
            'city',
            'latitude',
            'longitude',
        ]

class AdvertisementSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    location = LocationSerializer(many=False)
    category = CategorySerializer()
    class Meta:
        model = Advertisement
        fields = [
            'id',
            'title',
            'description',
            'category',
            'location',
            'created_at',
            'user',
        ]
