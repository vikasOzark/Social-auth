
# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('auth_profile.urls')),
#
# ]


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from auth_profile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("login/", views.login, name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path('social-auth/', include('social_django.urls', namespace="social")),
    # path("", views.home, name="home"),
    path('', include('auth_profile.urls')),
    path('accounts/', include('allauth.urls')),
]
'''
admin/
[name='home']
accounts/ signup/ [name='account_signup']
accounts/ login/ [name='account_login']
accounts/ logout/ [name='account_logout']
accounts/ password/change/ [name='account_change_password']
accounts/ password/set/ [name='account_set_password']
accounts/ inactive/ [name='account_inactive']
accounts/ email/ [name='account_email']
accounts/ confirm-email/ [name='account_email_verification_sent']
accounts/ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
accounts/ password/reset/ [name='account_reset_password']
accounts/ password/reset/done/ [name='account_reset_password_done']
accounts/ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
accounts/ password/reset/key/done/ [name='account_reset_password_from_key_done']
accounts/ social/
'''
