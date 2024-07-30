from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# CreateAPIView, ListAPIView, 
# from teleafya.serializers import teleafyaSerializer, teleafya
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, serializers
from appointments.pagination import CustomPageNumberPagination
from .serializers import BillingInformationSerializer
# BillingInformationSerializer, AppointmentSerializer 
from .models import BillingInformation, BookAppointment
# BillingInformation, Appointment
from appointments.permissions import IsOwner
from rest_framework.response import Response

# Create your views here.
class BillingInformationListAPIView(ListCreateAPIView):
    serializer_class = BillingInformationSerializer
    queryset = BillingInformation.objects.all()
    pagination_class = CustomPageNumberPagination
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Validate that the appointment exists before saving
        appointment_id = self.request.data.get('appointment')
        if not BookAppointment.objects.filter(id=appointment_id).exists():
            raise serializers.ValidationError({'appointment': 'Invalid appointment ID.'})
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class BillingInformationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BillingInformationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    lookup_field = "id"
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)