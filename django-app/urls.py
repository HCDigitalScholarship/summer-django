from django.contrib import admin
from django.urls import path
import summer2019_app.views as summer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', summer_views.index, name='index'),
]
