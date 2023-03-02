from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import boothcreater

boothcreate = boothcreater.as_view(
    {
        'put' : 'create',
        'get' : 'list',
    }
)

urlpatterns = [
    path('', views.booth_list),
    path('create/',boothcreate)
]

urlpatterns = format_suffix_patterns(urlpatterns)