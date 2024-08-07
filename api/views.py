from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from main.models import Customer, ProducerCategory, Energy, Transaction
from .serializers import CustomLoginSerializer, CustomerSerializer, ProducerCategorySerializer, EnergySerializer, TransactionSerializer

CustomUser = get_user_model()


import logging

class RegisterView(APIView):
    def post(self, request):
        logging.debug('Request data: %s', request.data)
        
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        postal_code = request.data.get('postal_code')
        password = request.data.get('password')

        if not (first_name and last_name and username and email and phone_number and postal_code and password):
            logging.error('Validation error: missing fields')
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            customer = Customer.objects.create(
                user=user, first_name=first_name, last_name=last_name, username=username, email=email, phone_number=phone_number, postal_code=postal_code)
            logging.info('User created successfully: %s', username)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error('Error creating user: %s', str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

CustomUser = get_user_model()

class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        # Debugging: Print the request data to see what is being received
        print("Request Data:", request.data)
        
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Debugging: Print extracted email and password
            print("Email:", email)
            print("Password:", password)
            
            try:
                user = CustomUser.objects.get(email=email)
                # Debugging: Print user info
                print("User found:", user)
                
                if user.check_password(password):
                    # Debugging: Print successful password check
                    print("Password check: Success")
                    
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'message': 'Login successful'
                    }, status=status.HTTP_200_OK)
                else:
                    # Debugging: Print failed password check
                    print("Password check: Failed")
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                # Debugging: Print user not found
                print("User does not exist")
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Debugging: Print the serializer errors to see why validation failed
            print("Serializer Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user



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
    # permission_classes = [IsAuthenticated]

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'message': 'Transactions retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            'message': 'Transaction created successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


