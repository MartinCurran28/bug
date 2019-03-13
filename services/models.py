from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, default='')
    description= models.TextField()
    price = models.DecimalField(mex_digits=6, deciminal_places=2)
    image = models.ImageField(upload_to='image')
    
def __str__(self):
    return self.image
