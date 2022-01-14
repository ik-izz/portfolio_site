from django.db import models

# Create your models here.
class exchange_rate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    #image = models.ImageField(upload_to='exchange_rate/images/')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title