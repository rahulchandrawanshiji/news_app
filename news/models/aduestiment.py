from django.db import models
class Aduestiment(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='static')
    about=models.CharField(max_length=300)

    def __str__(self):
        return self.name
