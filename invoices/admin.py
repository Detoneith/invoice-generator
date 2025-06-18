from django.contrib import admin
from .models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "total_amount")
    list_filter = ("created_at",)
    filter_horizontal = ("products",)

    def total_amount(self, obj):
        return sum(p.price for p in obj.products.all())

    total_amount.short_description = "Total (€)"
