from django.conf.urls import url,include
from Home import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]