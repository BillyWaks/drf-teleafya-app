from billing import views
from django.urls import path


urlpatterns = [
    
    path("", views.BillingInformationListAPIView.as_view(), name="billing"),
    path("<int:id>", views.BillingInformationDetailAPIView.as_view(), name="billing_information"),
    
]