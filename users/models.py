from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date
import string, random


# Payment Options
PAYMENT_OPTIONS = (
    ('ecocash', 'ECOCASH'),
    ('onemoney', 'ONE-MONEY'),
)


class BillingInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=10, help_text='Mobile Number - (e.g. 0776887606')
    paid_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=1)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_OPTIONS, default='ecocash')
    expire_date = models.DateField()
    reference_code = models.TextField()
    # Paynow Variables
    poll_url = models.TextField(null=True)
    payment_status = models.TextField(null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Billing Information'

    def save(self, *args, **kwargs):
        # Set an expiry date 30 days after payment
        self.expire_date = date.today() + timedelta(days=30)
        # Generate random string for reference code
        self.reference_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        super().save(*args, **kwargs)

    #TODO: Get Absolute URL here for the transaction details

