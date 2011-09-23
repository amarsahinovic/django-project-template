from django.db import models
from libs import utils

# Create your models here.

class CoreDummy(models.Model):
    dummy = models.CharField(max_length = 255)
    
    # Add default ordering
    class Meta: 
        ordering = ['id']
        