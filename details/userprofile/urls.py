from django.urls import path
from .views import MyPasswordChangeView, MyPasswordResetDoneView
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('new_account/', views.CreateNewAccount.as_view(), name='utilizator_nou'),
    path('change-password/', MyPasswordChangeView.as_view(), name='password-change-view'),
    path('change-password/done/', MyPasswordResetDoneView.as_view(), name='password-change-done-view'),
]
