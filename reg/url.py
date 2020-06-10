from django.urls import path
from . import views

urlpatterns = [
    path('',views.ho1, name='ho1'),
    path('sum',views.sum, name='sum'),

]