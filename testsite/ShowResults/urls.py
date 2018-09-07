from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from ShowResults import views

urlpatterns = [
    url(r'^continue_img', views.continue_img, name='continue_img'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^$', views.analyze, name='analyze'),
    url(r'^delete-image/(?P<id>\d+)/$',views.delete_image,name="delete_image"),
    url(r'^refresh', views.refresh, name='refresh'),
]

