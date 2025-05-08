""" @author Nathan Lee
@date 5/8/25 """
from django.urls import path
from .views import indexPageView
from .views import aboutPageView


urlpatterns = [

    path("", indexPageView, name="index"),    path("about/", aboutPageView, name="about"),




            ]