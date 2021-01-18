from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import Account
from project.models import Advertisement, Category, Location, Service, Review


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'district',
            'city',
            'latitude',
            'longitude',
        ]


class ServiceAdvertisementSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    location = LocationSerializer(many=False)

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        location = Location.objects.create(**location_data)
        validated_data["location"] = location
        validated_data["user"] = self.context["request"].user

        return super().create(validated_data)


class ServiceSerializer(ServiceAdvertisementSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'title',
            'description',
            'category',
            'location',
            'created_at',
            'user',
        ]


class AdvertisementSerializer(ServiceAdvertisementSerializer):
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


class ReviewSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'service',
            'user',
            'msg',
            'stars',
            'created_at'
        ]

    def create(self, validated_data):
        # Atribuir utilizador atual
        validated_data["user"] = self.context["request"].user

        return super().create(validated_data)
