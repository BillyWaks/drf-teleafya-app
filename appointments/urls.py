from appointments import views
from django.urls import path

urlpatterns = [
    path("", views.BookAppointmentListAPIView.as_view(), name="appointments"),
    path("<int:id>", views.BookAppointmentDetailAPIView.as_view(), name="book_appointment"),
    # path("", views.BillingInformationListAPIView.as_view(), name="appointments"),
    # path("<int:id>", views.BookAppointmentDetailAPIView.as_view(), name="billing_information"),
    # path("", views.AppointmentListAPIView.as_view(), name="appointments"),
    # path("<int:id>", views.AppointmentDetailAPIView.as_view(), name="appointment")
    
]