from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(db_index=True,max_length=111)
    slug = models.SlugField(db_index=True,max_length=111,unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=111)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

