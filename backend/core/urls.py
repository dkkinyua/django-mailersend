from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("home/", views.home, name="home"),
    path("send-email/", views.send_email_user, name="send-email"),
    path("logout/", views.logout, name='logout'),
]