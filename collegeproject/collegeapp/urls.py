from.import views
from django.urls import path





urlpatterns = [


    path('',views.home,name='home'),
    path('form',views.form,name='form'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('newpage',views.newpage,name='newpage'),
    path('message',views.message,name='message'),
    path('logout',views.logout,name='logout')
]
