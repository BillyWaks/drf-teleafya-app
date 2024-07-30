from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# CreateAPIView, ListAPIView, 
# from teleafya.serializers import teleafyaSerializer, teleafya
# from rest_framework.permissions import IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from appointments.pagination import CustomPageNumberPagination
from .serializers import PaymentSerializer 
from .models import Payment
from appointments.permissions import IsOwner
from rest_framework.response import Response

# Create your views here.
class PaymentListAPIView(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    # pagination_class = CustomPageNumberPagination
    permissions_classes = (permissions.IsAuthenticated,)
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, 
    #                    filters.OrderingFilter]

    # filterset_fields = ['user','phone_number','book_appointment','date','time','status']
    # search_fields = ['user','phone_number','book_appointment','date','time','status']
    # ordering_fields = ['user','phone_number','book_appointment','date','time','status']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)

class PaymentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    permissions_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return self.queryset.objects.filter(owner=self.request.user)