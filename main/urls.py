from django.urls import path
from . import views, HodViews

urlpatterns = [
    # Authentication URLs
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    
    # Admin home URL
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    
    # Customer management URLs
    path('add_customer/', HodViews.add_customer, name="add_customer"),
    path('add_customer_save/', HodViews.add_customer_save, name="add_customer_save"),
    path('edit_customer/<int:customer_id>/', HodViews.edit_customer, name="edit_customer"),
    # path('edit_customer_save/', HodViews.edit_customer_save, name="edit_customer_save"),  # Commented out
    path('manage_customer/', HodViews.manage_customer, name="manage_customer"),
    path('delete_customer/<int:customer_id>/', HodViews.delete_customer, name="delete_customer"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    
    # Admin profile URLs
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    
    # Energy management URLs
    path('manage_energy/', HodViews.manage_energy, name="manage_energy"),
    path('add_energy/', HodViews.add_energy, name="add_energy"),
    path('add_energy_save/', HodViews.add_energy_save, name="add_energy_save"),
    path('edit_energy/<int:energy_id>/', HodViews.edit_energy, name="edit_energy"),
    path('edit_energy_save/', HodViews.edit_energy_save, name="edit_energy_save"),
    path('delete_energy/<int:energy_id>/', HodViews.delete_energy, name="delete_energy"),
    
    # Producer category management URLs
    path('manage_producer_category/', HodViews.manage_producer_category, name="manage_producer_category"),
    path('add_producer_category/', HodViews.add_producer_category, name="add_producer_category"),
    path('add_producer_category_save/', HodViews.add_producer_category_save, name="add_producer_category_save"),
    path('edit_producer_category/<int:category_id>/', HodViews.edit_producer_category, name="edit_producer_category"),
    path('edit_producer_category_save/', HodViews.edit_producer_category_save, name="edit_producer_category_save"),
    path('delete_producer_category/<int:category_id>/', HodViews.delete_producer_category, name="delete_producer_category"),
    
    # Transaction management URLs
    path('manage_transaction/', HodViews.manage_transaction, name="manage_transaction"),
    path('add_transaction/', HodViews.add_transaction, name="add_transaction"),
    path('add_transaction_save/', HodViews.add_transaction_save, name="add_transaction_save"),
    path('edit_transaction/<int:transaction_id>/', HodViews.edit_transaction, name="edit_transaction"),
    path('edit_transaction_save/', HodViews.edit_transaction_save, name="edit_transaction_save"),
    path('delete_transaction/<int:transaction_id>/', HodViews.delete_transaction, name="delete_transaction"),


    path('get_csrf_token/', HodViews.get_csrf_token, name='get_csrf_token'),
    path('payment/create', HodViews.create_payment, name='create_payment'),
    path('payment/execute', HodViews.execute_payment, name='execute_payment'),
  
]
