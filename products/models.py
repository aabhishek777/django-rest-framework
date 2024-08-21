from django.db import models



class Products(models.Model):
    title=models.CharField(max_length=100)
    content= models.TextField(blank=True, null=True)
    price= models.DecimalField(decimal_places=2, max_digits=15, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f" (float((self.price)*80))

    class Meta:
        db_table= "products"
        
    def __str__(self):
        return f"{self.title,self.content,self.price}"   