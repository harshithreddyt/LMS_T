from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.ImageField(upload_to='static/images/books', null=True)
    summary = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('available', ('Available for issuing')),
        ('issued', ('Issued by someone')),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self) -> str:
        return self.name + " | " + self.author