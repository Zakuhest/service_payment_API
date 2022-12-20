from rest_framework import serializers
from pagos.models import Payment_user

class PaymentUserSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = 'payment_date',