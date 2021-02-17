from django.urls import path
from account.api import views

from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', views.LoginAccount.as_view(), name='login'),
    path('change_password/', views.UpdatePassword.as_view(), name='pass_update'),
    path('delete_account/', views.DeleteAccount.as_view(), name='delete_account')
]
