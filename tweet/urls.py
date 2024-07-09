from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index),
    path('tweet_list/',views.tweet_list,name='tweet_list'),
    path('create/',views.create_tweet,name='create_tweet'),
    path('edit/<int:tweet_id>/',views.edit_tweet,name='edit_tweet'),
    path('delete/<int:tweet_id>/',views.delete_tweet,name='delete_tweet'),
    path('signup/',views.signup_view,name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
