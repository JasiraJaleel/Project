from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Student"

class Items(models.Model):
    name=models.CharField(max_length=250)
    designation=models.TextField()
    img=models.ImageField(upload_to="pics")

    class Meta:
        verbose_name_plural="Items"

    def __str__(self):
        return self.name

class Movies(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField()
    year=models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to="pics")

    class Meta:
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name
