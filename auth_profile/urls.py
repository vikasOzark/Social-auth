from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('accounts/', include('allauth.urls')),
]
