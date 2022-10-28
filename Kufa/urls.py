
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admiin/', admin.site.urls),
    path('', include("kodia.urls")),
]
