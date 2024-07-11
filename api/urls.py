from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, CustomerDetailView, ProducerCategoryListView, EnergyListView, TransactionListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/create/', RegisterView.as_view(), name='create_user'),
    path('users/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customers/', CustomerDetailView.as_view(), name='customer_detail'),
    path('producer-categories/', ProducerCategoryListView.as_view(), name='producer_category_list'),
    path('energy/', EnergyListView.as_view(), name='energy_list'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
]
