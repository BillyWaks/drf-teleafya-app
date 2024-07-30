# from helpers.models import TrackingModel
from django.db import models
from authentication.models import User
from django.core.exceptions import ValidationError

def validate_age(value):
    if not (0 <= value <= 99):
        raise ValidationError('Age must be between 0 and 99.')
    
def validate_id_number(value):
    if not (0 <= value <= 99999999):
        raise ValidationError('ID number must be up to 8 digits long.')

class BookAppointment(models.Model):
    BOOK_FOR_CHOICES = [
        ('MYSELF', 'Myself'),
        ('OTHER', 'Other'),
    ]

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]

    SERVICE_CHOICES = [
        ('GENERAL CONSULTATION', 'General consultation'),
        ('MODERN LAB', 'Modern lab'),
        ('PHARMACY', 'Pharmacy'),
        ('SPECIALIST', 'Specialist services'),
    ]

    APPOINTMENT_TYPE_CHOICES = [
        ('PHYSICAL', 'Physical'),
        ('VIRTUAL', 'Virtual'),
    ]

    STATUS_CHOICES = [
        ('APPROVED', 'Approved'),
        ('NOT APPROVED', 'Not approved'),
    ]

    book_for = models.CharField(max_length=6, choices=BOOK_FOR_CHOICES)
    id_number = models.PositiveIntegerField(validators=[validate_id_number])
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES)
    appointment_type = models.CharField(max_length=8, choices=APPOINTMENT_TYPE_CHOICES)
    age = models.PositiveIntegerField(validators=[validate_age])
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    area_of_residence = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.book_for} (ID: {self.id_number})"

# class BillingInformation(models.Model):
#     appointment = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     paybill = models.CharField(max_length=255)
#     acc_number = models.CharField(max_length=255)
#     billing_id = models.AutoField(primary_key=True)

#     def __str__(self):
#         return f"Billing Information (Billing ID: {self.billing_id}, Service: {self.appointment.service})"

# class Appointment(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)
#     book_appointment = models.ForeignKey(BookAppointment, on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()
#     status = models.CharField(max_length=12, choices=BookAppointment.STATUS_CHOICES)

#     def __str__(self):
#         return f"Appointment for {self.user.full_name} on {self.date} at {self.time}"





    # def __str__(self):
    #     return self.title    
    
#     # Create your models here.
# class teleafya(TrackingModel):
#     title = models.CharField(max_length=255)
#     desc = models.TextField()
#     is_complete = models.BooleanField(default=False)
#     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title
    