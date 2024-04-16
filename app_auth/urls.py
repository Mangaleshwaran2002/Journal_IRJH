from django.urls import path
from .views import login_page,create_author,logout_page
urlpatterns = [
    path('login', login_page,name='login page'),
    path('logout', logout_page,name='logout_page'),
    path('singup', create_author,name='author_signup'),
]