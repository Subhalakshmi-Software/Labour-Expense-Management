from django import forms
from .models import BankAccounts, LabourDetails, LabourExpense, Workplace


class LabourDetailsForm(forms.ModelForm):
    class Meta:
        model = LabourDetails
        fields = "__all__"


class BankAccountsForm(forms.ModelForm):
    class Meta:
        model = BankAccounts
        fields = "__all__"


class LabourExpenseForm(forms.ModelForm):
    expense_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = LabourExpense
        exclude = ("bank_account",)
        fields = "__all__"


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = "__all__"
