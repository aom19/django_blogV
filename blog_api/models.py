from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000 )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    small_description = models.CharField(max_length=200)
    tags= models.CharField(max_length=200)
    type= models.CharField(max_length=200)
    trending = models.BooleanField(default=False)



    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name