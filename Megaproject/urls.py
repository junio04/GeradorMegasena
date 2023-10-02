
from django.contrib import admin
from django.urls import path
from core.views import mega

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mega, name= 'mega')
]
