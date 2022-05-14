from django.urls import path
from . import views

urlpatterns =[
    path('sayhi1', views.sayhi1, name="welcome"),
    path('sayhi2', views.sayhi2, name="happybirthday"),
    path('sayhi3', views.sayhi3, name="happynewyear"),
    path('sayhi4/<myname>', views.sayhi4, name="namewelcome"),
    path('sayhi5/<myname>', views.sayhi5, name="namehappybirthday"),
    path('sayhi6/<myname>', views.sayhi6, name="now")
]