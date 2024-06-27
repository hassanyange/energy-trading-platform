from django.urls import path
from .views import RegisterView, LoginView, CustomerDetailView, CompanyListView, ProducerCategoryListView, ProducerListView, EnergyListView, TransactionListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer/', CustomerDetailView.as_view(), name='customer_detail'),
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('producer-categories/', ProducerCategoryListView.as_view(), name='producer_category_list'),
    path('producers/', ProducerListView.as_view(), name='producer_list'),
    path('energy/', EnergyListView.as_view(), name='energy_list'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
]
