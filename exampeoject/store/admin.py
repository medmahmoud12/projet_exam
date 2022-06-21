from django import urls
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import Booking , Contact, Album, Artist

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"

class BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = (
        (None, {'fields': ('album','contacted','cantact_at',)}),)
    list_filter =('create_at','created')
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]

admin.site.register(Booking)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']

# Register your models here.
