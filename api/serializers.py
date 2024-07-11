from rest_framework import serializers
from main.models import Customer, ProducerCategory, Energy, Transaction
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

CustomUser = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = CustomUser.objects.filter(email=email).first()
        if user is not None and user.check_password(password) and user.is_active:
            attrs['username'] = user.username
            return super().validate(attrs)
        else:
            raise serializers.ValidationError('No active account found with the given credentials')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'postal_code', 'created_at', 'updated_at']

class ProducerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerCategory
        fields = ['name', 'address', 'contact_email', 'contact_phone', 'description', 'created_at', 'updated_at']

class EnergySerializer(serializers.ModelSerializer):
    producer = ProducerCategorySerializer()

    class Meta:
        model = Energy
        fields = ['producer', 'capacity', 'available_units', 'cost_per_unit', 'timestamp']

class TransactionSerializer(serializers.ModelSerializer):
    energy = EnergySerializer()

    class Meta:
        model = Transaction
        fields = ['consumer', 'energy', 'requested_units', 'total_cost', 'timestamp']
