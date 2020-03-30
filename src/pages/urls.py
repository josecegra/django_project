from django.urls import path
from . import views

urlpatterns = [
    path('',views.result_view,name='home'),
    path('about/',views.about,name='about'),
    ]