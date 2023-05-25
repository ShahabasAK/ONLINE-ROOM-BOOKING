from django.urls import path
from . import views
urlpatterns = [

    # pages-name,action of that  page,name=default

    # path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('' ,views.homepage ,name='homepage'),


    path('user_home', views.user_home, name="user_home"),
    path('logout', views.logout, name="logout"),
    path('adminhome', views.adminhome , name="adminhome"),
    path('addrooms', views.addrooms, name="addrooms"),
    path('profile', views.profile, name='profile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('viewroom', views.viewroom, name='viewroom'),
    path('updateroom/<str:pk>',views.updateroom, name='updateroom'),
    path('deleteroom/<int:room_id>/', views.deleteroom,name='deleteroom'),
    path('about', views.about, name='about'),
    path('userroom', views.userroom, name='userroom'),




]
