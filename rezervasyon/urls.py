
from django.urls import path
from . import views


app_name = 'rezervasyon'
urlpatterns = [
    path('', views.rezervasyon_islemleri, name= 'rezervasyon islemleri'),
]