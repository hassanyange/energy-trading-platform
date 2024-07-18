from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from main.models import CustomUser, Customer, Energy, Transaction, ProducerCategory
from .forms import AddCustomerForm,  EditCustomerForm, AddEnergyForm, EditEnergyForm, AddProducerCategoryForm, EditProducerCategoryForm, AddTransactionForm,  EditTransactionForm

def admin_home(request):
    all_customer_count = Customer.objects.all().count()
    all_energy_count = Energy.objects.all().count()
    all_transaction_count = Transaction.objects.all().count()
    
    customer_name_list = []
    customers = Customer.objects.all()
    for customer in customers:
        customer_name_list.append(customer.first_name)

    context = {
        "all_customer_count": all_customer_count,
        "all_energy_count": all_energy_count,
        "all_transaction_count": all_transaction_count,
        "customer_name_list": customer_name_list,
    }
    return render(request, "hod_template/home_content.html", context)


def manage_energy(request):
    energies = Energy.objects.all()
    context = {
        "energies": energies
    }
    return render(request, 'hod_template/manage_energy_template.html', context)

def add_energy(request):
    form = AddEnergyForm()
    producers = ProducerCategory.objects.all()
    context = {
        'form': form,
        'producers': producers,
    }
    return render(request, 'hod_template/add_energy_template.html', context)

def add_energy_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_energy')
    else:
        form = AddEnergyForm(request.POST)

        if form.is_valid():
            capacity = form.cleaned_data['capacity']
            available_units = form.cleaned_data['available_units']
            cost_per_unit = form.cleaned_data['cost_per_unit']
            producer = form.cleaned_data['producer']

            try:
                energy = Energy(
                    capacity=capacity,
                    available_units=available_units,
                    cost_per_unit=cost_per_unit,
                    producer=producer
                )
                energy.save()

                messages.success(request, "Energy Added Successfully!")
                return redirect('manage_energy')
            except Exception as e:
                messages.error(request, f"Failed to Add Energy: {e}")
                return redirect('add_energy')
        else:
            messages.error(request, "Form is not valid")
            return redirect('add_energy')

def edit_energy(request, energy_id):
    energy = get_object_or_404(Energy, id=energy_id)
    form = EditEnergyForm(instance=energy)
    producers = ProducerCategory.objects.all()
    context = {
        "form": form,
        "id": energy_id,
        "producers": producers,
    }
    return render(request, "hod_template/edit_energy_template.html", context)

def edit_energy_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        energy_id = request.POST.get('energy_id')
        energy = get_object_or_404(Energy, id=energy_id)

        form = EditEnergyForm(request.POST, instance=energy)
        if form.is_valid():
            form.save()
            messages.success(request, "Energy Updated Successfully!")
            return redirect('/edit_energy/'+str(energy_id))
        else:
            messages.error(request, "Form is not valid")
            return redirect('/edit_energy/'+str(energy_id))

def delete_energy(request, energy_id):
    energy = get_object_or_404(Energy, id=energy_id)
    try:
        energy.delete()
        messages.success(request, "Energy Deleted Successfully.")
        return redirect('manage_energy')
    except Exception as e:
        messages.error(request, f"Failed to Delete Energy: {e}")
        return redirect('manage_energy')

def manage_producer_category(request):
    categories = ProducerCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'hod_template/manage_producer_category_template.html', context)

def add_producer_category(request):
    if request.method == "POST":
        form = AddProducerCategoryForm(request.POST)
    else:
        form = AddProducerCategoryForm(initial={
            'contact_email': 'example@example.com',
            'contact_phone': '074xxxxxxx'
        })

    context = {
        'form': form
    }
    return render(request, 'hod_template/add_producer_category_template.html', context)

def add_producer_category_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_producer_category')
    else:
        form = AddProducerCategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Producer Category Added Successfully!")
                return redirect('manage_producer_category')
            except Exception as e:
                messages.error(request, f"Failed to Add Producer Category: {e}")
                return redirect('add_producer_category')
        else:
            messages.error(request, "Form is not valid")
            return redirect('add_producer_category')


def edit_producer_category(request, category_id):
    category = get_object_or_404(ProducerCategory, id=category_id)
    form = AddProducerCategoryForm(instance=category)
    context = {
        "form": form,
        "category": category,  # Pass the category object to the template
        "id": category_id,
    }
    return render(request, "hod_template/edit_producer_category_template.html", context)


def edit_producer_category_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        category_id = request.POST.get('category_id')
        category = get_object_or_404(ProducerCategory, id=category_id)
        form = AddProducerCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Producer Category Updated Successfully!")
            return redirect('/edit_producer_category/'+str(category_id))
        else:
            messages.error(request, "Form is not valid")
            return redirect('/edit_producer_category/'+str(category_id))
        


def delete_producer_category(request, category_id):
    category = get_object_or_404(ProducerCategory, id=category_id)
    try:
        category.delete()
        messages.success(request, "Producer Category Deleted Successfully.")
        return redirect('manage_producer_category')
    except Exception as e:
        messages.error(request, f"Failed to Delete Producer: {e}")
        return redirect('manage_producer_category')

def manage_transaction(request):
    transactions = Transaction.objects.all()
    context = {
        "transactions": transactions
    }
    return render(request, 'hod_template/manage_transaction_template.html', context)

def add_transaction(request):
    form = AddTransactionForm()
    context = {
        'form': form
    }
    return render(request, 'hod_template/add_transaction_template.html', context)

def add_transaction_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_transaction')
    else:
        form = AddTransactionForm(request.POST)

        if form.is_valid():
            consumer = form.cleaned_data['consumer']
            energy = form.cleaned_data['energy']
            requested_units = form.cleaned_data['requested_units']
            total_cost = form.cleaned_data['total_cost']

            try:
                transaction = Transaction(
                    consumer=consumer,
                    energy=energy,
                    requested_units=requested_units,
                    total_cost=total_cost
                )
                transaction.save()

                messages.success(request, "Transaction Added Successfully!")
                return redirect('manage_transaction')
            except Exception as e:
                messages.error(request, f"Failed to Add Transaction: {e}")
                return redirect('add_transaction')
        else:
            messages.error(request, "Form is not valid")
            return redirect('add_transaction')

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    form = EditTransactionForm(instance=transaction)
    context = {
        "form": form,
        "id": transaction_id,
    }
    return render(request, "hod_template/edit_transaction_template.html", context)

def edit_transaction_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        transaction_id = request.POST.get('transaction_id')
        transaction = get_object_or_404(Transaction, id=transaction_id)

        form = EditTransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction Updated Successfully!")
            return redirect('/edit_transaction/'+str(transaction_id))
        else:
            messages.error(request, "Form is not valid")
            return redirect('/edit_transaction/'+str(transaction_id))

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    try:
        transaction.delete()
        messages.success(request, "Transaction Deleted Successfully.")
        return redirect('manage_transaction')
    except Exception as e:
        messages.error(request, f"Failed to Delete Transaction: {e}")
        return redirect('manage_transaction')

def add_customer(request):
    form = AddCustomerForm()
    context = {
        'form': form,
    }
    return render(request, 'hod_template/add_customer_template.html', context)

def add_customer_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_customer')
    else:
        form = AddCustomerForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
 

            try:
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    user_type=2  # Assuming '2' is for Consumers
                )

                messages.success(request, "Customer Added Successfully!")
                return redirect('add_customer')
            except Exception as e:
                messages.error(request, f"Failed to Add Customer: {e}")
                return redirect('add_customer')
        else:
            messages.error(request, "Form is not valid")
            return redirect('add_customer')

def manage_customer(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers
    }
    return render(request, 'hod_template/manage_customer_template.html', context)

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    form = EditCustomerForm(instance=customer.user)
    
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, instance=customer.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Updated Successfully!")
            return redirect('manage_customer')
        else:
            messages.error(request, "Form is not valid")
    
    context = {
        "form": form,
        "id": customer_id,
        "username": customer.user.username,
    }
    return render(request, "hod_template/edit_customer_template.html", context)

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    try:
        customer.user.delete()
        messages.success(request, "Customer Deleted Successfully.")
    except Exception as e:
        messages.error(request, f"Failed to Delete Customer: {e}")
    return redirect('manage_customer')






@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')




from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt, get_token
import paypalrestsdk
import logging


logger = logging.getLogger(__name__)


paypalrestsdk.configure({
    "mode": "sandbox",  # Sandbox or live
    "client_id": 'ASnwQzBkPndV_fr93YE5-GpxKI5YHaZPcSE4Pgtokd1Xpqi8tuOuAIHjQqI4ErTuoiGXo8rDQvzMTA0g',
    "client_secret": 'EPGhkm_WFs3-WdBFRiusdInNVSBsZ_nDHle6CHK2BCpIpHsq4r4SkkZ9mXcO8bNXOGAJGZuu47UBbH5q'
})

@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

@csrf_exempt
def create_payment(request):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },

        "redirect_urls": {
            "return_url": "https://energy-trading-platform.onrender.com/payment/execute",
            "cancel_url": "https://energy-trading-platform.onrender.com/payment/cancel"
        },

        "transactions": [{
            "amount": {
                "total": "10.00",
                "currency": "USD"
            },
            "description": "This is the payment transaction description."
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return JsonResponse({"approval_url": approval_url})
    else:
        return JsonResponse({"error": payment.error}, status=500)

@csrf_exempt
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    logger.info(f"Executing payment with ID: {payment_id} and Payer ID: {payer_id}")

    if not payment_id or not payer_id:
        return JsonResponse({"error": "Missing paymentId or PayerID"}, status=400)

    try:
        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            logger.info("Payment executed successfully.")
            return JsonResponse({"status": "Payment successful"})
        else:
            logger.error(f"Payment execution failed: {payment.error}")
            return JsonResponse({"error": payment.error}, status=500)
    except paypalrestsdk.exceptions.ResourceNotFound as e:
        logger.error(f"Resource not found: {str(e)}")
        return JsonResponse({"error": "Payment not found"}, status=404)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)