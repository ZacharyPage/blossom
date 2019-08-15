from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('user/', include('django.contrib.auth.urls')),
    path('register/', views.UserFormView.as_view(), name='register')
]
