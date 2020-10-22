from api.user.models import CustomUser
from django.db import models
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    product_name = models.CharField(max_length=500)
    total_products = models.CharField(max_length=500, default=0)
    transation_id = models.CharField(max_length=150, default=0)
    total_amount = models.CharField(max_length=50, default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
