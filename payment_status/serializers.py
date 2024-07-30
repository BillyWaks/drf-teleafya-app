from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment
        fields = ('user','phone_number','book_appointment','date','time','status')