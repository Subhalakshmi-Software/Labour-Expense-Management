from django.contrib import admin
from .models import BankAccounts, LabourDetails, LabourExpense

admin.site.register(BankAccounts)
admin.site.register(LabourDetails)
admin.site.register(LabourExpense)
