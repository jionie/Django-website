from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from myaccount import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', views.login, name='login'),
]


