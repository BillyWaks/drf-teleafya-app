from rest_framework import serializers
from .models import BillingInformation
from appointments.models import BookAppointment

class BillingInformationSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(queryset=BookAppointment.objects.all())
    class Meta:
        model = BillingInformation
        fields = ['appointment', 'amount', 'paybill', 'acc_number', 'billing_id', 'owner']
        read_only_fields = ['billing_id', 'owner']  # Mark owner as read-only if set automatically
