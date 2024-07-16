from teleafya.views import teleafyaAPIView, teleafyaDetailAPIView
from django.urls import path

urlpatterns = [
    path("", teleafyaAPIView.as_view(), name="teleafya"),
    path("<int:id>", teleafyaDetailAPIView.as_view(), name="teleafya")
    
]