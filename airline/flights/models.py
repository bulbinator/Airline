from django.db import models

# Create your models here.

# Create a class for each SQL table you need





class Flight(models.Model):
    origin = models.CharField(max_length=64) #origin coloum will be the name of the airport, and does not exceede 64 characters
    destination = models.CharField(max_length=64) 
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
