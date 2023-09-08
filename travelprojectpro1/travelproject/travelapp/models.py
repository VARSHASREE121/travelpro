from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class guide(models.Model):
    gname=models.CharField(max_length=250)
    gimg=models.ImageField(upload_to='gpics')
    gdesc=models.TextField()
    gnum=models.CharField(max_length=12)

    def __str__(self):
        return self.gname