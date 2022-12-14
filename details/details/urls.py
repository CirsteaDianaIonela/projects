"""details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from userprofile import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# from userprofile.views import MyLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login', views.custom_login, name='login'),
    # path('logout', views.custom_logout, name='logout'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'), #este partea de logout veche
    # path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', views.my_login, name='login'),
    path('visualizations/', include('aplicatie1.urls')),
    # path('profile/', include('userprofile.urls')), #am comentat cand am facut noul virtual venv, totul merge ok
    path('userprofile/', include('userprofile.urls'), name='userprofile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
