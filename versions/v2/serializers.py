from rest_framework import serializers
from pagos.models import Payment_user, Services, Expired_payments

class PaymentUserSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = 'payment_date',

class ServicesSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ExpiredPaymentsSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = '__all__'