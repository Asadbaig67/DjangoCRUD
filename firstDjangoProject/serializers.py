from rest_framework import serializers
from User.models import User, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    images = ImageSerializer(
        many=True, read_only=True
    )  # Add this field to store multiple images

    class Meta:
        model = User
        fields = "__all__"
