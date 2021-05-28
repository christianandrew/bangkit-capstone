from django.urls import path
#from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getCount.as_view()),
    path('judul/', views.listTitle.as_view()),
    path('upload/', views.dariAndroid.as_view()),
]