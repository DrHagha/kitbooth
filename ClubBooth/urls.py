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

##전체 정보 조회(http://127.0.0.1:8000/booth/all/)(req: {} -> res : {{id : 1, booth_name : ddd, booth_location : s23}, {...}} )
#특정 데이터 조회(http://127.0.0.1:8000/booth/detail/<int:pk>)(req : {} -> res : {name : dd, ddd: sss, ...})
urlpatterns = format_suffix_patterns(urlpatterns)