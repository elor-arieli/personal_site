from django.conf.urls import url,include
from Lynn import views

app_name = 'Lynn'

urlpatterns = [
    url(r'about/',views.about,name='about'),
    url(r'CV/',views.CV,name='CV'),
    url(r'MD/',views.MD,name='MD'),
    url(r'art/',views.art,name='art'),
    url(r'photography/',views.photography,name='photography'),
    url(r'music/',views.music,name='music'),
]





