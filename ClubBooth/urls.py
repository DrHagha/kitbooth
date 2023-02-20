from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('all/', views.booth_list),
    path('detail/<int:pk>/', views.booth_detail)
]

##전체 정보 조회(http://127.0.0.1:8000/booth/all/)(req: {} -> res : {{id : 1, booth_name : ddd, booth_location : s23}, {...}} )
#특정 데이터 조회(req : {id : 1} -> res : {name : dd, ddd: sss, ...})
urlpatterns = format_suffix_patterns(urlpatterns)