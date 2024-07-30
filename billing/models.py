from django.db import models
from appointments.models import BookAppointment
from authentication.models import User

class BillingInformation(models.Model):
    appointment = models.ForeignKey(BookAppointment, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paybill = models.CharField(max_length=20)
    acc_number = models.CharField(max_length=20)
    billing_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Regular ForeignKey field

    def __str__(self):
        return (f"Billing Information (Billing ID: {self.billing_id}, "
                f"Amount: {self.amount}, Paybill: {self.paybill}, "
                f"Account Number: {self.acc_number})")