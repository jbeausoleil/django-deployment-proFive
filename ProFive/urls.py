from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path

from appFive import views

urlpatterns = [
    re_path(r'^$', view=views.index, name='index'),
    path('admin/', view=admin.site.urls),
    re_path(r'^app-five/', include('appFive.urls')),
    re_path(r'^logout/$', view=views.user_logout, name='logout'),
    re_path(r'^special/', view=views.special, name='special')
]
