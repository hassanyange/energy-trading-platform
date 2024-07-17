from rest_framework import serializers
from main.models import Customer, ProducerCategory, Energy, Transaction
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from rest_framework import generics

CustomUser = get_user_model()




class CustomLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'postal_code', 'created_at', 'updated_at']

class ProducerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerCategory
        fields = ['name', 'address', 'contact_email', 'contact_phone', 'description', 'created_at', 'updated_at']


class EnergySerializer(serializers.ModelSerializer):
    producer = serializers.SerializerMethodField()

    class Meta:
        model = Energy
        fields = ['cost_per_unit', 'available_units', 'producer']

    def get_producer(self, obj):
        return obj.producer.name  # Only return the name field


class TransactionSerializer(serializers.ModelSerializer):
    energy = EnergySerializer()

    class Meta:
        model = Transaction
        fields = ['consumer', 'energy', 'requested_units', 'total_cost', 'timestamp']
