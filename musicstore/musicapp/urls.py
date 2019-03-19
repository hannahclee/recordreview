from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('records/', views.records, name='records'),
    path('artists/', views.artists, name='artists'),
    path('recorddetail/<int:id>', views.recorddetail, name='details'),
    path('newRecord/', views.newRecord, name='newrecord'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    ]