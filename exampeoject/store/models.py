from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)

    def __str__(self):
        return self.name
    class meta:
         verbose_name = "Artiste"
    

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class meta:
         verbose_name = "contact"

class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title
    class meta:
         verbose_name = "album"

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete = models.CASCADE)
    album = models.OneToOneField(Album,on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.contact.name
    class meta:
         verbose_name = "Réservation"













#ARTISTS = {
#    'francis-cabrel': {'name': 'Francis Cabrel'},
#    'lej': {'name': 'Elijay'},
#    'rosana': {'name': 'Rosana'},
 #   'maria-dolores-pradera': {'name': 'Maria Dolores Pradera'},
#}

#ALBUMS = [
#    {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
##   {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'],ARTISTS['maria-dolores-pradera']]},
#]