from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    # these items will be showed in django admin listings page
    list_display = ('id', 'title', 'state', 'realtor', 'is_published', 'price', 'list_date')
    # if you want to connect link with an item to open it, list it here below
    list_display_links = ('id','title')
    # for filter or soting, list column names here
    list_filter = ('realtor','state')
    # to make a field editable list it here
    list_editable = ('is_published',)
    # set search fields here
    search_fields = ('title','description','address','city','state','zipcode')
    # set number of list to show per page
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)
