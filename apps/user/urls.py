from django.urls import path
from apps.user import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),  ###Ruta para el registro
    path('profile/', views.profile, name='profile'),  ###Perfil del usuario (requiere login)
    path('', views.user, name='user'),  ###Página de usuario
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  ###Login
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(), 
         name='password_reset'),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(), 
         name='password_reset_complete'),
]
