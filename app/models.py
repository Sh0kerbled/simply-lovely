from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.title

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='products_images/')

    def __str__(self):
        return self.title