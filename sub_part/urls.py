from django.urls import path 
from . import views 

urlpatterns=[ 
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),
    path('promo',views.promo,name='promo'),
    
]