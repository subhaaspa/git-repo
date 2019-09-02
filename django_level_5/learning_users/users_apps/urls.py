from django.urls import path
from users_apps import views

app_name = 'users_apps'

urlpatterns = [
    path('register',views.register,name="register"),
    path('login/',views.user_login,name="user_login"),
    path('logout/',views.user_logout,name="user_logout")
]
