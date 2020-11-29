from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('myspace/', views.myspace, name='myspace'),
    path('game/<int:game_id>', views.game, name='game')
]
