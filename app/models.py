from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=50, null=False)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.title