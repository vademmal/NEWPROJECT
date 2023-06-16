from django.db import models

# Create your models here.
class place(models.Model): # name of table
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def __str__(self):
         return self.name

class team(models.Model):
    tname = models.CharField(max_length=250)
    timg = models.ImageField(upload_to='pics')
    tdesc = models.TextField()

    def __str__(self):
         return self.tname

