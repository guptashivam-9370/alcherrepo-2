from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name= "alcher-home"),
    path("page1/",views.page1,name= "alcher-page1"),
    path("page2/",views.page2,name= "alcher-page2"),
]