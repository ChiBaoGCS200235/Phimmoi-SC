from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexclass.as_view(), name="Index"),
    path('login/', views.loginclass.as_view(), name="login"),
    path('signup/', views.signupclass.as_view(), name="signup"),
    path('theloai/', views.theloaiclass.as_view(), name="type"),
    path('xem-phim/<int:movie_id>', views.watchclass.as_view(), name="watch"),
    path('home/', views.userclass.as_view(), name="user"),
    path('home/theloai/', views.usertheloaiclass.as_view(), name="usertheloai"),
]