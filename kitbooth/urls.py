from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('booth/', include('ClubBooth.urls')),
    path('guestbook/', include('GuestBook.urls'))
]
