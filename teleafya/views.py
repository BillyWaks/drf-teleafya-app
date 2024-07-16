from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from teleafya.serializers import teleafyaSerializer, teleafya
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class teleafyaAPIView(ListCreateAPIView):
    serializer_class = teleafyaSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return teleafya.objects.filter(owner=self.request.user)

class teleafyaDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = teleafyaSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    
    def get_queryset(self):
        return teleafya.objects.filter(owner=self.request.user) 