from django.db import models

# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    # def Meta:
    #     verbose_name_plural='cities'