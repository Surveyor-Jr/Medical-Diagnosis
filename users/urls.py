from django.urls import path, include
from users import views as user_views
from .views import Billing

urlpatterns = [   
    # App Views
    path('', user_views.home, name='profile-home'),
    path('billing/', Billing.as_view(), name='billing'),
    path('billing/payment/', user_views.pay_subscription, name='make-payment'),
]