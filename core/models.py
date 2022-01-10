from django.db import models


class BankAccounts(models.Model):
    account_number = models.CharField(max_length=100, primary_key=True)
    account_holder_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return self.account_holder_name


class LabourDetails(models.Model):
    fullname = models.CharField(primary_key=True, max_length=200)
    bank_account = models.ForeignKey(BankAccounts, on_delete=models.RESTRICT)
    aadhar_number = models.CharField(max_length=10)
    home_address = models.TextField(max_length=100)
    mobile_number = models.CharField(max_length=13)
    
    def __str__(self):
        return self.fullname


class Workplace(models.Model):
    unit_name = models.CharField(primary_key=True, max_length=200)
    unit_address = models.TextField(max_length=100)
    
    def __str__(self):
        return self.unit_name


class LabourExpense(models.Model):
    labour_name = models.ForeignKey(LabourDetails, on_delete=models.RESTRICT)
    bank_account = models.ForeignKey(BankAccounts, on_delete=models.RESTRICT)
    workplace = models.ForeignKey(Workplace, on_delete=models.RESTRICT)
    expense_date = models.DateField()
    amount = models.FloatField()

    def save(self, *args, **kwargs):
        self.bank_account = self.labour_name.bank_account
        super(LabourExpense, self).save(*args, **kwargs)

    def __str__(self):
        return (
            self.expense_date.strftime("%Y-%m-%d") + " : " + self.labour_name.fullname
        )
