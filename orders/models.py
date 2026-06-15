from django.db import models

class Order(models.Model):
    phone = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    delivery_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    remind = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Замовлення №{self.id} — {self.phone}"

class OrderItem(models.Model):
    # При видаленні замовлення видаляються і його товари
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    weight = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product_name} ({self.flavor}) x {self.quantity}"