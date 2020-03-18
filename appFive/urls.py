from django.conf.urls import re_path
from appFive import views

app_name = 'appFive'

urlpatterns = [
    re_path(r'^register', view=views.register, name='register' ),
    re_path(r'^user-login/$', view=views.user_login, name='user_login' ),
]