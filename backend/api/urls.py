from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView



from userauths.views import  (
    MytokenObtainApiView,
    RegisterApiView,
    PasswordEmailVerify,
    PasswordChangeView,   
                              )


urlpatterns = [
    path('user/token/',MytokenObtainApiView.as_view()),
    path('user/register/',RegisterApiView.as_view()),
    path('user/refresh/', TokenRefreshView.as_view(),),
    path('user/password-reset/<email>/',PasswordEmailVerify.as_view()),
    path('user/password-change/',PasswordChangeView.as_view()),
    
]
