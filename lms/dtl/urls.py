from django.urls import path 

from . import views

urlpatterns = [
    path('demo/', views.dtl_demo, name='dtl_demo'),
]