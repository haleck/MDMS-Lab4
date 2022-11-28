from rest_framework import serializers

from userprofile.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'
