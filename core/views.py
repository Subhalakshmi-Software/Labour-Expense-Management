from django.shortcuts import render
from django_tables2.export.export import TableExport
from django_tables2.config import RequestConfig
from core.filters import LabourExpenseFilter
from .forms import BankAccountsForm, LabourDetailsForm, LabourExpenseForm, WorkplaceForm
from .tables import BankAccountsTable, LabourDetailsTable, LabourExpenseTable, WorkplaceTable
from .models import BankAccounts, LabourDetails, LabourExpense, Workplace
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect

@permission_required("core.bank_accounts.can_add_bank_accounts")
@login_required
def bank_accounts_entry(request):
    if request.method == "POST":
        form = BankAccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = BankAccountsForm()
    return render(request, "form_entry.html",{"form": form,"form_name": "Bank Accounts Entry"})

@permission_required("core.labour_details.can_add_labour_details")
@login_required
def labour_details_entry(request):
    if request.method == "POST":
        form = LabourDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = LabourDetailsForm()
    return render(request, "form_entry.html",{"form": form,"form_name": "Labour Details Entry"})

@permission_required("core.labour_expense.can_add_labour_expense")
@login_required
def labour_expense_entry(request):
    if request.method == "POST":
        form = LabourExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = LabourExpenseForm()
    return render(request, "form_entry.html",{"form": form,"form_name": "Labour Expense Entry"})

@permission_required("core.workplace.can_add_workplace")
@login_required
def workplace_entry(request):
    if request.method == "POST":
        form = WorkplaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:
        form = WorkplaceForm()
    return render(request, "form_entry.html",{"form": form,"form_name": "Workplace Entry"})

@login_required
def labour_expense_report(request):
    Filter = LabourExpenseFilter(request.GET, queryset=LabourExpense.objects.all())
    table = LabourExpenseTable(Filter.qs)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("labour_expense_report.{}".format(export_format))
    return render(request, "report.html", {"table": table, "filter": Filter, "report_name": "Labour Expense Report"})

@login_required
def labour_details_report(request):
    table = LabourDetailsTable(LabourDetails.objects.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("labour_details_report.{}".format(export_format))
    return render(request, "report.html", {"table": table, "report_name": "Labour Details Report"})

@login_required
def bank_accounts_report(request):
    table = BankAccountsTable(BankAccounts.objects.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("bank_accounts_report.{}".format(export_format))
    return render(request, "report.html", {"table": table, "report_name": "Bank Accounts Report"})

@login_required
def workplace_report(request):
    table = WorkplaceTable(Workplace.objects.all())
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("workplace_report.{}".format(export_format))
    return render(request, "report.html", {"table": table, "report_name": "Workplace Report"})

@login_required
def success(request):
    return render(request, "success.html")

def home(request):
    return render(request, "welcome.html")

def view_404(request, exception=None):
    return redirect('/home')

