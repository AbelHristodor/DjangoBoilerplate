from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', views.send_msg_view),
    path('', views.home_view, name="homepage")
]
