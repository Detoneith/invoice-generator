from django.db import models
from products.models import Product

class Invoice(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='invoices')

    def __str__(self):
        return f"Facture #{self.id} du {self.created_at:%d/%m/%Y}"
    
    def total(self):
        return sum(p.price for p in self.products.all())

    class Meta:
        ordering = ['-created_at']