from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title