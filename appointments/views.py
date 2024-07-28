from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# CreateAPIView, ListAPIView, 
# from teleafya.serializers import teleafyaSerializer, teleafya
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
# from teleafya.pagination import CustomPageNumberPagination
from .serializers import BookAppointmentSerializer, BillingInformationSerializer, AppointmentSerializer 
from .models import BookAppointment, BillingInformation, Appointment
from .permissions import IsOwner


# Create your views here.
class BookAppointmentListAPIView(ListCreateAPIView):
    serializer_class = BookAppointmentSerializer
    queryset = BookAppointment.objects.all()
    # pagination_class = CustomPageNumberPagination
    permissions = (permissions.IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, 
    #                    filters.OrderingFilter]

    # filterset_fields = ['book_for','id_number','service','appointment_type','age','gender','area_of_residence']
    # search_fields = ['book_for','id_number','service','appointment_type','age','gender','area_of_residence']
    # ordering_fields = ['book_for','id_number','service','appointment_type','age','gender','area_of_residence']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class BookAppointmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookAppointmentSerializer
    permissions = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)


class BillingInformationListAPIView(ListCreateAPIView):
    serializer_class = BillingInformationSerializer
    queryset = BillingInformation.objects.all()
    # pagination_class = CustomPageNumberPagination
    permissions = (permissions.IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, 
    #                    filters.OrderingFilter]

    # filterset_fields = ['appointment','amount','paybill','acc_number','billing_id']
    # search_fields = ['appointment','amount','paybill','acc_number','billing_id']
    # ordering_fields = ['appointment','amount','paybill','acc_number','billing_id']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)

class BillingInformationDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BillingInformationSerializer
    permissions = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user) 


class AppointmentListAPIView(ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    # pagination_class = CustomPageNumberPagination
    permissions = (permissions.IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, 
    #                    filters.OrderingFilter]

    # filterset_fields = ['user','phone_number','book_appointment','date','time','status']
    # search_fields = ['user','phone_number','book_appointment','date','time','status']
    # ordering_fields = ['user','phone_number','book_appointment','date','time','status']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)

class AppointmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permissions = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)