from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone', 'company', 'current_role', 'birth_date',
                  'date_joined')
        extra_kwarg = {'password': {'write_only': True}}


class AiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiModel
        fields = ('title', 'description', 'url', 'creation_datetime', 'description_summery', 'api_code')


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('request_time', 'user_id', 'ai_model_id')


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('user_id', 'ai_model_id')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'ai_model_tag')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('ai_model_id', 'img_url')


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('ai_model_id', 'user_id', 'stars')
