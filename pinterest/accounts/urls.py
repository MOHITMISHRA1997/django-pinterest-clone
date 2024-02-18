from django.urls import path,include


app_name = "accounts"
from . import views
urlpatterns = [
    path("changepassword/",views.change_password,name= "change_password"),
    path("signup/",views.user_register,name= "signup"),
    path("login/",views.user_login,name= "login"),
    path("logout/",views.user_logout,name= "logout"),
    path("follow/<str:username>",views.follow,name= "follow"),
    path("profile/_saved/<str:username>/",views.profile,name= "profile"),
    path("unfollow/<str:username>",views.un_follow,name= "unfollow"),
    path("edit-profile/",views.EditUserProfile,name="edit_profile"),
    path('forgot_password/', include('django.contrib.auth.urls')),
]
