import django_filters
from django import forms
from .models import LabourExpense


class LabourExpenseFilter(django_filters.FilterSet):
    expense_date__gt = django_filters.DateFilter(
        field_name="expense_date",
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="gt",
        label='Start Date:',
    )
    expense_date__lt = django_filters.DateFilter(
        field_name="expense_date",
        widget=forms.DateInput(attrs={"type": "date"}),
        lookup_expr="lt",
        label='End Date:',
    )

    class Meta:
        model = LabourExpense
        fields = []
