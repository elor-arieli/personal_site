from django.conf.urls import url,include
from Elor import views

app_name = 'Elor'

urlpatterns = [
    url(r'about/',views.about,name='about'),
    url(r'CV/',views.CV,name='CV'),
    url(r'photography/',views.photography,name='photography'),
    url(r'public_appearence/',views.public_appearence,name='public_appearence'),
    url(r'writing/', views.writing, name='writing'),
]