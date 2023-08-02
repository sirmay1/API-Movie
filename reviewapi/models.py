from django.db import models

from django.db import models

class TV(models.Model):
    film = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    
   
    def __str__(self):
        return self.film + ' | ' + self.genre +  ' | ' + self.network + ' | ' + str(self.year) + ' | ' + str(self.rating)



#NOTE: For the ratings I should had used an IntegerField instead of a FloatField, this was the wrong Field for the project. Later I will look into figuring out a way to revise it. 07/28/2023