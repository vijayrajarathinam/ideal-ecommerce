from rest_framework.serializers import ModelSerializer
from .models import Order, OrderItem

class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity']

class OrderItemSerializers(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'user', 'status', 'created_at', 'items']
