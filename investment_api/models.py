from django.db import models

# Create your models here.
class Investment_API(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name
