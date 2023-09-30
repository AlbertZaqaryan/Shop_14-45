from django.db import models

# Create your models here.


class HomeLogo(models.Model):

    logo = models.ImageField('HomeLogo', upload_to='images')



class HomeCarusel(models.Model):
    title = models.CharField('Carusel title', max_length=100)
    name = models.CharField('Carusel name', max_length=100)
    about = models.TextField('Carusel text')
    img = models.ImageField('Carusel image', upload_to='images')
    logo = models.ImageField('Carusel logo', upload_to='images')

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categ')
    name = models.CharField('SubCategory name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'



class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_prod')
    sale = models.BooleanField('Product sale')
    new = models.BooleanField('New product')

    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Image')
    sale_logo = models.ImageField('Sale logo')
    new_logo = models.ImageField('new logo')
    price = models.PositiveIntegerField('Price')

    def __str__(self):
        return self.name