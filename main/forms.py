from django import forms
from main.models import CustomUser, Customer, Energy, Transaction, ProducerCategory

class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'user_name',  'email', 'phone_number')

class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'user_name', 'email', 'phone_number')

class AddEnergyForm(forms.ModelForm):
    class Meta:
        model = Energy
        fields = ('type', 'capacity', 'available_units', 'cost_per_unit', 'producer')

class EditEnergyForm(forms.ModelForm):
    class Meta:
        model = Energy
        fields = ('type', 'capacity', 'available_units', 'cost_per_unit', 'producer')

class AddProducerCategoryForm(forms.ModelForm):
    class Meta:
        model = ProducerCategory
        fields = ('name', 'description')

class EditProducerCategoryForm(forms.ModelForm):
    class Meta:
        model = ProducerCategory
        fields = ('name', 'description')

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('consumer', 'energy', 'requested_units', 'total_cost')

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('consumer', 'energy', 'requested_units', 'total_cost')
    
