# from django.db.models import fields
from rest_framework import serializers
from .models import User, Post


class ChatListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ChatItemSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ChatItemCreateSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'


  