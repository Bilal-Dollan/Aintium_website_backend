from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import *


class UserCreateSerializer(serializers.ModelSerializer):
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'company', 'current_role', 'birth_date')


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'company', 'current_role', 'birth_date')
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
            'phone': {'required': True},
            'birth_date': {'required': True},
        }

    def validate_phone(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(phone=value).exists():
            raise serializers.ValidationError({"Phone": "This number is already in use."})
        return value

    def update(self, instance, validated_data):

        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.phone = validated_data['phone']
        instance.company = validated_data['company']
        instance.current_role = validated_data['current_role']
        instance.birth_date = validated_data['birth_date']

        instance.save()

        return instance


class ResetPasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password')

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"new_password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class AiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiModel
        fields = ('id', 'title', 'description', 'url', 'image_url', 'creation_datetime', 'description_summery', 'api_code')


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


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('ai_model_id', 'user_id', 'stars')
