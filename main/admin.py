from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Customer,  ProducerCategory,  Energy, Transaction


admin.site.register(CustomUser)
admin.site.register(AdminHOD)
admin.site.register(Customer)
admin.site.register(ProducerCategory)
admin.site.register(Energy)
admin.site.register(Transaction)

