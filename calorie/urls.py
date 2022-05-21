from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name="home"),
  path('searchfoodcalorie',views.dashboard,name="dashboard"),
  path('view<str:pk>',views.view,name='viewit'),
  path('delete_order<str:pk>',views.remove,name='delete'),
]
