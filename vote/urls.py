from django.urls import path
from vote import views
from django.contrib.auth.views import logout_then_login

app_name = 'vote'


urlpatterns = [
    path('login', views.AuthLoginView.as_view(), name='login'),
    path('results/', views.result, name='result'),
    path('logout/',logout_then_login, name='logout'),
    path('index/', views.Index.as_view(), name='index'),
    path('', views.Index.as_view(), name='index')
]