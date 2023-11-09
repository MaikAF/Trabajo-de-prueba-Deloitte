from django.db import models

class   Categoria(models.Model):
        id = models.BigAutoField(primary_key=True)
        category = models.CharField(max_length=50)

        def __str__(self) -> str:
                return self.category    


class   Producto(models.Model):
        id = models.BigAutoField(primary_key=True)
        product_name = models.CharField(max_length=50)
        image_url = models.CharField(max_length=200)
        price = models.FloatField()
        category = models.ForeignKey(Categoria , on_delete=models.CASCADE)

        def __str__(self) -> str:
                return self.product_name