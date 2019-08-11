from django.urls import path
from vote import views
from django.contrib.auth.views import logout_then_login

app_name = 'vote'


urlpatterns = [
    path('login', views.AuthLoginView.as_view(), name='login'),
    path('results/', views.ResultView.as_view(), name='result'),
    path('logout/',logout_then_login, name='logout'),
    path('', views.IndexView.as_view(), name='index')
]
