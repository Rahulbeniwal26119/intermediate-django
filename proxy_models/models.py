from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)

class ArchivedProducts(Product):
    objects = CustomManager()

    class Meta:
        proxy = True
        verbose_name = 'Archived Product'
        verbose_name_plural = 'Archived Products'
    
    
class LatestProducts(Product):

    class Meta:
        proxy = True
        verbose_name = 'Latest Product'
        verbose_name_plural = 'Latest Products'
        ordering = ['-created_at']


class ProductLegacy(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'proxy_models_product'

    def __str__(self):
        return self.name


class ProductLegacyProxy(ProductLegacy):
    class Meta:
        proxy = True
        verbose_name = 'Product Legacy'
        verbose_name_plural = 'Products Legacy'
        ordering = ['-created_at']