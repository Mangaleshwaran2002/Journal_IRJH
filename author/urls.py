from django.urls import path
from .views import index,Manuscript_status,Manuscript_submit

urlpatterns = [
    path('', index,name='index'),
    # path('login', login,name='login page'),
    path('Manuscript_status/', Manuscript_status,name='Manuscript_status'),
    path('Manuscript_submit/', Manuscript_submit,name='Manuscript_submit'),
]