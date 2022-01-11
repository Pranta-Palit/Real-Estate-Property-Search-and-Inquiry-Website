from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'), #put all htmls urls here
    path('about', views.about, name='about'),
]