from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'id': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        '''create and return a new user'''
        user = User.objects.create_user(
            email=validated_data.get('email'),
            full_name=validated_data.get('full_name'),
            password=validated_data.get('password')
        )
        return user

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password should be at least 8 characters')
        return value
