from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='goods_images')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка')
    quantitiy = models.PositiveIntegerField(default=0, verbose_name='Количество')
    description = models.TextField(default='Описание', verbose_name='Описание')
    number_of_sales = models.IntegerField(default=0, verbose_name='Кол-во продаж')
    category = models.ForeignKey(to=Categories, on_delete=models.SET_DEFAULT, default='Special', verbose_name='Категория')

    


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
