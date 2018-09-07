from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from imageUpload import views

urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^clear', views.clear, name='clear'),
    url(r'^delete-Image/(?P<id>\d+)/$',views.delete_Image,name="delete_Image"),
]
