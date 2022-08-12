from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login_ok/', views.login_ok, name='login_ok'),
    path('register/', views.register, name='register'),
    path('register_ok/', views.register_ok, name='register_ok'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('modal/<str:selected_theme>/', views.modal, name='modal'),
    path('test/', views.test, name='test'),
    path('play/<str:selected_theme>/<int:selected_rounds>', views.play, name='play'),
    path('winner/<str:selected_theme>/<str:selected_name>/<int:rounds>', views.winner, name='winner'),
    path('ranking/<str:selected_theme>', views.ranking, name='ranking'),
    path('info/<str:user_id>', views.info, name='info'),
    path('edit/<str:user_id>', views.edit, name='edit'),
    path('edit_ok/<str:user_id>', views.edit_ok, name='edit_ok'),
    path('deleteAcc/<str:user_id>', views.deleteAcc, name='deleteAcc'),
]