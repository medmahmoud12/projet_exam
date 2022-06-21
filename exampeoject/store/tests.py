from turtle import title
from django.test import TestCase

from django.urls import reverse

from .models import Album, Artist, Booking, Contact

#page d'accueil renvoit un code de status 200

class PageIndex(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class PageDetailTest(TestCase):

    # setup est une methode qui s'execute avant chaque test unitaire
    def setUp(self):
        progression = Album.objects.create(title = "bonne progression de la methode")
        self.album = Album.objects.get(title = "bonne progression de la methode")

    # la page detail renvoit un code de statut 200 si le items demandé existe

    def test_page_detail_renvoit_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    #la page detail renvoit un code de status 404 si l'items demandé n'existe pas

    def test_page_detail_renvoit_200(self):
        album_id = self.album.id + 1
        response = self.client.get(reverse('detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)

class PageReservationTest(TestCase):

    def setUp(self):
        Contact.objects.create(name="ledebaye", email="ledebaye@gmail.com")
        album1 = Album.objects.create(title="bonne progression de la methode")
        artist1 = Artist.objects.create(name="Tekno")
        album1.artists.add(artist1)
        self.album = Album.objects.get(title='bonne progression de la methode')
        self.contact = Contact.objects.get(name='ledebaye')

    
    #une requete est executée si une nouvelle reservation est bien ajoutée dans la base de données

    def test_dajout_reservation(self):
        old_bookings = Booking.objects.count()
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings + 1)

    #Test q'une reservation est bien liée a un album

    def test_reservation_liee_album(self):
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.album, booking.album)

    #Test q'une reservation est bien liée a un contact

    def test_reservation_liee_contact(self):
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        booking = Booking.objects.first()
        self.assertEqual(self.contact, booking.contact)
    
    #Un album n'est plus disponible quand il a ete reservé

    def test_album_nonDisponible_apres_reservation(self):
        album_id = self.album.id
        name = self.contact.name
        email =  self.contact.email
        response = self.client.post(reverse('detail', args=(album_id,)), 
        {
            'name': name,
            'email': email
        })

        self.album.refresh_from_db()
        self.assertFalse(self.album.available)




