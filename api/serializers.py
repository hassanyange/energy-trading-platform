from rest_framework import serializers
from main.models import Customer,  ProducerCategory,  Energy, Transaction
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'user_name', 'email', 'phone_number', 'created_at', 'updated_at']



class ProducerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProducerCategory
        fields = ['name', 'description', 'created_at', 'updated_at']


class EnergySerializer(serializers.ModelSerializer):
    producer = ProducerCategorySerializer()

    class Meta:
        model = Energy
        fields = ['producer', 'type', 'capacity', 'available_units', 'cost_per_unit', 'timestamp']

class TransactionSerializer(serializers.ModelSerializer):
    energy = EnergySerializer()

    class Meta:
        model = Transaction
        fields = ['consumer', 'energy', 'requested_units', 'total_cost', 'timestamp']
