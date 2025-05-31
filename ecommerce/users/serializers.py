from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'phone_number', 'name',
            'contract_info', 'shipping_address', 'billing_address',
            'payment_info', 'role', 'email_verified', 'phone_verified'
        ]