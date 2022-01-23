from django.contrib import admin
from .models import *


class BillingAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone', 'expire_date')
    search_fields = ('user', 'email', 'phone')


admin.site.register(BillingInformation, BillingAdmin)
