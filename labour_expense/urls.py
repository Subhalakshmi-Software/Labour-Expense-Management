from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view()),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("success", views.success),
    path("home", views.home),
    path("labour_details_entry", views.labour_details_entry),
    path("labour_expense_entry", views.labour_expense_entry),
    path("labour_expense_report", views.labour_expense_report),
    path("labour_details_report", views.labour_details_report),
    path("bank_accounts_report", views.bank_accounts_report),
    path("bank_accounts_entry", views.bank_accounts_entry),
    path("bank_accounts_entry", views.bank_accounts_entry),
    path("workplace_entry", views.workplace_entry),
    path("workplace_report", views.workplace_report),
]

handler404 = 'core.views.view_404'