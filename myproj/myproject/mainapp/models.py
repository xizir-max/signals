from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='Категория',
                                 related_name='products')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'