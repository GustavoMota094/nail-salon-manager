from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'user', 'phone_number', 'notes')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        
        return customer

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            
            if 'password' in user_data:
                user.set_password(user_data['password'])
            
            user.save()

        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        
        return instance
    