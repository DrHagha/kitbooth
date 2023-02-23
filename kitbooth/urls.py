from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#스웨거 세팅 정보
schema_view = get_schema_view(
    openapi.Info(
        title="동아리 부스 홍보 사이트",
        default_version='0.0',
        # description="해당 문서 설명(예: humanscape-project API 문서)",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="이메일"), # 부가정보
        # license=openapi.License(name="mit"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #스웨거 적용코드
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    path('admin/', admin.site.urls),
    path('booth', include('ClubBooth.urls')),
    path('guestbook', include('GuestBook.urls'))
]
