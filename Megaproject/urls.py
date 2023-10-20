from django.contrib import admin
from django.urls import path
from core.views import mega
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mega, name= 'mega'),
    path('404/', TemplateView.as_view(template_name='404.html', name='404'))

]