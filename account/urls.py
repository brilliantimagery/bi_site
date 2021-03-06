"""bi_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, reverse_lazy, reverse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views as account_views

app_name = 'account'

urlpatterns = [
    # path('login/', views.login_request, name='login'),
    # path('logout/', views.logout_request, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',
                                              success_url=reverse_lazy('account:password_reset_done'),
                                              email_template_name='account/password_reset_email.html',
                                              ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
                                                     success_url=reverse_lazy('account:password_reset_complete'),
                                                     ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('privacy-policy', account_views.privacy_policy, name='privacy_policy'),
    path('profile/', account_views.profile, name='profile'),
    path('register/', account_views.register, name='register'),
]
