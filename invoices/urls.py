from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView

app_name = "invoices"

urlpatterns = [
    path("", InvoiceListView.as_view(), name="list"),
    path("new/", InvoiceCreateView.as_view(), name="create"),
    path("<int:pk>/", InvoiceDetailView.as_view(), name="detail"),
]