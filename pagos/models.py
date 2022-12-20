from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Payment_user(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="service")
    amount = models.FloatField(default=0.0)
    payment_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True)

class Expired_payments(models.Model):
    pay_user_id = models.ForeignKey(Payment_user, on_delete=models.CASCADE, related_name="payment_user")
    penalty_fee_amount = models.FloatField(default=0.0)