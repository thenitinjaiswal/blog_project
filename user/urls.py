from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('registers/',views.user_register,name='registers'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')
]
