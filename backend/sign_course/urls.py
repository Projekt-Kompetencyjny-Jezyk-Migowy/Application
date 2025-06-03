# sign_course/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Users & Auth
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Course structure
    path('sections/', views.list_sections, name='list_sections'),
    path('sections/<int:section_id>/', views.section_detail, name='section_detail'),
    path('sections/<int:section_id>/unlock/', views.unlock_section, name='unlock_section'),

    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/complete/', views.complete_lesson, name='complete_lesson'),

    # Progress
    path('progress/', views.get_user_progress, name='get_user_progress'),
]