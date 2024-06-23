from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Customer, Company, ProducerCategory, Producer, Energy, Transaction


class UserModel(UserAdmin):
    pass




class ProducerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'category', 'created_at')
    search_fields = ('user__username', 'company__name', 'category__name')

class EnergyAdmin(admin.ModelAdmin):
    list_display = ('producer', 'type', 'capacity', 'available_units', 'cost_per_unit', 'timestamp')
    search_fields = ('producer__user__username', 'type')
    list_filter = ('type', 'producer__company')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'energy', 'requested_units', 'total_cost', 'timestamp')
    search_fields = ('consumer__username', 'energy__type')
    list_filter = ('energy__type', 'timestamp')

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHOD)
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(ProducerCategory)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Energy, EnergyAdmin)
admin.site.register(Transaction, TransactionAdmin)

