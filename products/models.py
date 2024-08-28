from django.db import models

from decimal import Decimal


class Products(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.80)

    @property
    def discount(self):
        sale_price = Decimal(self.sale_price)
        return "%.2f" % (float(self.price - sale_price))

    class Meta:
        db_table = "products"

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Price: {self.price}, Sale Price: {self.sale_price},  get_discount: {self.get_discount}"
