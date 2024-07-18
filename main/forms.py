from django import forms
from main.models import CustomUser, Customer, Energy, Transaction, ProducerCategory

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username',  'email', 'phone_number', 'postal_code')

class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'postal_code')

class AddEnergyForm(forms.ModelForm):
    class Meta:
        model = Energy
        fields = ( 'capacity', 'available_units', 'cost_per_unit', 'producer')

class EditEnergyForm(forms.ModelForm):
    class Meta:
        model = Energy
        fields = ('capacity', 'available_units', 'cost_per_unit', 'producer')

class AddProducerCategoryForm(forms.ModelForm):
    class Meta:
        model = ProducerCategory
        fields = ('name', 'description', 'contact_email', 'contact_phone')

 
class EditProducerCategoryForm(forms.ModelForm):
    class Meta:
        model = ProducerCategory
        fields = ('name', 'description', 'contact_email', 'contact_phone')

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('Mobile_network', 'phone_number', 'total_cost')

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('Mobile_network', 'phone_number', 'total_cost')