from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'total_price', 'payment_method', 'created_at')
    inlines = [OrderItemInline] # Покаже товари прямо всередині замовлення