from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Customer"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    

class AdminHOD(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    postal_code = models.CharField(max_length = 15, default=11442)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.user.user_type = 2  # Set user_type to 2 for customers
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class ProducerCategory(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(default='Dar es Salaam')
    contact_email = models.EmailField(default="example@example.com")
    contact_phone = models.CharField(max_length=15, default='074xxxxxxx')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Energy(models.Model):
    producer = models.ForeignKey(ProducerCategory, on_delete=models.CASCADE)
    capacity = models.FloatField()  # in kWh
    available_units = models.FloatField()  # in kWh
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # in bitcoins
    timestamp = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    consumer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 2})
    energy = models.ForeignKey(Energy, on_delete=models.CASCADE)
    requested_units = models.FloatField()  # in kWh
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)  # in bitcoins
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_cost = self.requested_units * self.energy.cost_per_unit
        super().save(*args, **kwargs)
