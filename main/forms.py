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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default values for initial display
        self.fields['contact_email'].initial = 'example@example.com'
        self.fields['contact_phone'].initial = '074xxxxxxx'

class EditProducerCategoryForm(forms.ModelForm):
    class Meta:
        model = ProducerCategory
        fields = ('name', 'description', 'contact_email', 'contact_phone')

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('consumer', 'energy', 'requested_units', 'total_cost')

class EditTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('consumer', 'energy', 'requested_units', 'total_cost')
    
