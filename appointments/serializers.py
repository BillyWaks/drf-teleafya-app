from rest_framework import serializers
from .models import BookAppointment
# BillingInformation, Appointment


class BookAppointmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = BookAppointment
        fields = ('book_for','id_number','service','appointment_type','age','gender','area_of_residence')

# class BillingInformationSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = BillingInformation
#         fields = ('appointment','amount','paybill','acc_number','billing_id')

# class AppointmentSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = Appointment
#         fields = ('user','phone_number','book_appointment','date','time','status')