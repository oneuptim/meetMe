from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
   url(r'^$', views.index),
   url(r'^register_process$', views.register_process),
   url(r'^login$', views.login),
   url(r'^login_process$', views.login_process),
   url(r'^dashboard$', views.dashboard),
   # url(r'^users/new$', views.new_user_process),
   # url(r'^users/edit$', views.update_user_process),
   # url(r'^users/show(?P<id>\d+)$', views.show),
   # url(r'^users/edit(?P<id>\d+)$', views.edit), #for admin
   url(r'^logout$', views.logout),
]
