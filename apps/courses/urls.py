from . import views
from django.urls import path


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('detail/', views.course_detail, name='course_detail'),
    path('lessons/', views.course_lessons, name='course_lessons'),
]
