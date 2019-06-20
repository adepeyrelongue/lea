from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts/',views.post_list,name='post-list'),
    path('posts/<slug:slug>/',views.post_detail,name='post-detail')
]
