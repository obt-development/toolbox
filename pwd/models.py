from django.db import models



class Generator(models.Model):
    
    
    
    
    title =  models.CharField(max_length=255)
    username =  models.CharField(max_length=255)
    url =  models.URLField(blank=True, null=True)
    
    pwd = models.CharField(max_length=100, blank=True, null=True)
    sixmonths = models.BooleanField(default=False)
    twelvemonths = models.BooleanField(default=True)
    caracteres = models.BooleanField(default=False)
    lettres = models.BooleanField(default=True)
    chiffres = models.BooleanField(default=True)
    validity_date = models.DateField(blank=True, null=True)

    
    def __str__(self):
        return self.title
    
    