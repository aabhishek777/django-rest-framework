from django.db import models
from decimal import Decimal

from django.conf import settings


USER = settings.AUTH_USER_MODEL


class Products(models.Model):

    user = models.ForeignKey(USER, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99)
    email = models.EmailField(null=True, blank=True)

    @property
    def sale_price(self):
        # Convert the percentage and result to Decimal
        calc = self.price * Decimal('0.80')
        return f'{calc:.2f}'

    @property
    def discount(self):
        # Ensure sale_price is used as a Decimal
        sale_price = Decimal(self.sale_price)
        discount_value = self.price - sale_price
        return f'{discount_value:.2f}'

    class Meta:
        db_table = "products"

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Price: {self.price}, Sale Price: {self.sale_price}, Discount: {self.discount}"
