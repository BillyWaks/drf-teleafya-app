from django.db import models
from authentication.models import User
from appointments.models import BookAppointment

class Payment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    book_appointment = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=12, choices=BookAppointment.STATUS_CHOICES)

    def __str__(self):
        return f"Payment for {self.user.get_full_name()} on {self.date} at {self.time}"
