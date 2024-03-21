from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (
    ('Statinonary', 'Statinonary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length = 20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    
    def __str__(self) -> str:
        return f'{self.name}-{self.quantity}'

class Orrder(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    order_quantity = models.PositiveIntegerField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str(self):
        return f'{self.product} order by {self.staff.username}'