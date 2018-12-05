from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor', 'city')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'city')
    search_fields = ('title', 'address', 'descrption',
                     'state', 'zipcode', 'price', 'city')
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
