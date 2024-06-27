from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from main.models import Customer, Company, ProducerCategory, Producer, Energy, Transaction
from .serializers import CustomerSerializer, CompanySerializer, ProducerCategorySerializer, ProducerSerializer, EnergySerializer, TransactionSerializer


User = get_user_model()
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        
        if not (username and password and email and first_name and last_name and phone_number):
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            customer = Customer.objects.create(
                user_name=username, email=email, first_name=first_name, last_name=last_name, phone_number=phone_number)
            customer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CustomerDetailView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.customer

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class ProducerCategoryListView(generics.ListCreateAPIView):
    queryset = ProducerCategory.objects.all()
    serializer_class = ProducerCategorySerializer
    permission_classes = [IsAuthenticated]

class ProducerListView(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
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
