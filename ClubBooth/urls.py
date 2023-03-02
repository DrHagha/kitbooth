from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import boothcreater

boothcreate = boothcreater.as_view(
    {
        'put' : 'create',
        'get' : 'list',
        'patch' : 'partial_update',
        'delete' : 'destroy',
    }
)

urlpatterns = [
    path('', views.booth_list),
    path('create/',boothcreate),
    path('destroy/<int:pk>/',boothcreate),
]

urlpatterns = format_suffix_patterns(urlpatterns)