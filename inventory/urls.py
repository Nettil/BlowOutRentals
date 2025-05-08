""" @author Nathan Lee
@date 5/8/25 """
from django.urls import path
from .views import instrumentsPageView, trumpetPageView



urlpatterns = [

    path("instruments/", instrumentsPageView, name="instruments"),    path("trumpet/", trumpetPageView, name="trumpet"),




            ]