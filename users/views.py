from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from MedicalDiagnosis.settings import paynow
from .forms import UserRegisterForm, PaymentForm
from .models import BillingInformation
import time


@login_required
def home(request):
    return render(request, 'users/profile.html')


# user registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created. Login now')
            return redirect('profile-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class Billing(LoginRequiredMixin, ListView):
    model = BillingInformation
    template_name = 'users/billing.html'
    context_object_name = 'billing'


@login_required
def pay_subscription(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone')
            price = form.cleaned_data.get('price')
            email = form.cleaned_data.get('email')
            payment_method = form.cleaned_data.get('payment_method')

            payment = paynow.create_payment('Order #100', email)
            payment.add('Medical Diagnosis Subscription', price)
            # Save response from Paynow
            response = paynow.send_mobile(payment, phone_number, payment_method)

            if response.success:
                # Save this to DB
                poll_url = response.poll_url
                # Payment Status
                # instructions = response.instructions #TODO: What does this really do?

                # Check status of transaction
                status = paynow.check_transaction_status(poll_url)  # TODO: Check Payment State Before saving

                if status.paid:

                    time.sleep(30)

                    # Save the data to the DB
                    instance = form.save(commit=False)
                    instance.user = request.user  # attach user profile
                    instance.poll_url = poll_url  # PayNow variable
                    instance.payment_status = status  # Paynow Variable
                    instance.payment_method = payment_method
                    instance.save()
                    # Tell user it was great
                    messages.success(request, f"You subscription worth {price} has been paid successfully")
                    return redirect('billing')

                else:
                    messages.info(request, "The transaction has failed.")
                    return redirect('make-payment')

    else:
        form = PaymentForm()
    return render(request, template_name='users/pay_sub.html', context={
        'form': form
    })
