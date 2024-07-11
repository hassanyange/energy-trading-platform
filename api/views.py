from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from main.models import Customer, ProducerCategory, Energy, Transaction
from .serializers import CustomTokenObtainPairSerializer, CustomerSerializer, ProducerCategorySerializer, EnergySerializer, TransactionSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

CustomUser = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        postal_code = request.data.get('postal_code')
        
        if not (username and password and email and first_name and last_name and phone_number and postal_code):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            customer = Customer.objects.create(
                user=user, first_name=first_name, last_name=last_name, username=username, email=email, phone_number=phone_number, postal_code=postal_code)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.customer

class ProducerCategoryListView(generics.ListCreateAPIView):
    queryset = ProducerCategory.objects.all()
    serializer_class = ProducerCategorySerializer
    permission_classes = [IsAuthenticated]

class EnergyListView(generics.ListCreateAPIView):
    queryset = Energy.objects.all()
    serializer_class = EnergySerializer
    permission_classes = [IsAuthenticated]

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(consumer=self.request.user)
