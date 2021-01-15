from rest_framework import serializers

from accounts.models import Account
from project.models import Advertisement, Category, Location


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['username', 'name', 'biography', 'contact', 'website', 'account_type', 'password', 'email']

    def create(self, validated_data):
        user: Account = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


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
