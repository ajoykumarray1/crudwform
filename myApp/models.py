from django.db import models

# Create your models here.
class Employee(models.Model):
    pro_pic=models.ImageField(upload_to='image')
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self):
        return self.name
