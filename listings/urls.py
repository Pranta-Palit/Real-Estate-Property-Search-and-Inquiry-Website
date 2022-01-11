from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'), #put all htmls urls here, this one is home url
    path('<int:listing_id>', views.listing, name='listing'), # we will show all listed home like listings/23, ans so need a int id
    path('search', views.search, name='search'),# it will look like listings/search
]