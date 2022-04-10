from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Generator(models.Model):
    
    title =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255)
    url =  models.URLField(blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True) 
    validity_date = models.DateField(blank=True, null=True)
    
    sixmomth = models.BooleanField(default=False)
    twelvesmonth = models.BooleanField(default=False)
    
    number_digits = models.IntegerField(default=4, validators=[MinValueValidator(4), MaxValueValidator(99)])

    resnum = models.BooleanField(default=False)
    reschar = models.BooleanField(default=False)
    resspec = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    