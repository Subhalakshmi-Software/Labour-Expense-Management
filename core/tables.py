import django_tables2 as tables
from .models import *


class LabourDetailsTable(tables.Table):
    class Meta:
        model = LabourDetails


class LabourExpenseTable(tables.Table):
    expense_date = tables.DateColumn(short=False)

    class Meta:
        model = LabourExpense


class BankAccountsTable(tables.Table):
    class Meta:
        model = BankAccounts


class WorkplaceTable(tables.Table):
    class Meta:
        model = Workplace
