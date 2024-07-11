from django.urls import path
from .views import CustomLoginView, RegisterView, UserDetailView, CustomerDetailView, ProducerCategoryListView, EnergyListView, TransactionListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', RegisterView.as_view(), name='create_user'),
    path('users/login/', CustomLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customers/', CustomerDetailView.as_view(), name='customer_detail'),
    path('producer-categories/', ProducerCategoryListView.as_view(), name='producer_category_list'),
    path('energy/', EnergyListView.as_view(), name='energy_list'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
]
