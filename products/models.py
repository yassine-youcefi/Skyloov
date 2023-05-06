from django.db import models


class Products(models.Model):

    name = models.CharField(max_length=255)

    brand = models.CharField(max_length=255, blank=True,
                             null=True, default=None)

    description = models.TextField(blank=True, null=True, default=None)

    category = models.CharField(max_length=255, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0.00)
    
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)

    image = models.ImageField(upload_to='products/', blank=True,
                              null=True, default=None)
    
    rating = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = 'Products'
        indexes = [
            models.Index(fields=['name'])
        ]
