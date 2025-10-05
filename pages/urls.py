from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcement_list/', views.announcement_list, name='announcement_list'),
    path('announcement_detail/<int:id>/', views.announcement_detail, name='announcement_detail'),
]