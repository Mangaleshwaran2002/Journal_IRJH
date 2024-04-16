from django.urls import path
from .views import editor_dashboard,accept_manuscript,reject_manuscript
urlpatterns = [
    path('', editor_dashboard,name='editor_dashboard'),
    # path('login', login,name='login page'),
    path('accept/<int:id>', accept_manuscript,name='accept_Manuscript'),
    path('reject/<int:id>', reject_manuscript,name='reject_Manuscript'),
]