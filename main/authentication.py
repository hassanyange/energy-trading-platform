# your_app/authentication.py

from rest_framework.authentication import TokenAuthentication

class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'Token'  # Customize the keyword if needed
