from payment_status import views
from django.urls import path

urlpatterns = [
    path("", views.PaymentListAPIView.as_view(), name="payment_status"),
    path("<int:id>", views.PaymentDetailAPIView.as_view(), name="payment")
]